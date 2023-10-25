%
% A SIMPLE MPEG LIKE DECODING OF SEQUENTIAL IMAGERY
%
% current_image - current uint8 image to encode
% reference_image - image to compare to to determine which 8x8 regions need
%                   updating. If empty then encode the entire image.
% Q - quality factor to employ in compression
%
% huff_encoded - Huffman encoded data (created by Huff06.m)
% updated_reference - updated reference image.
%

function new_image = simple_dmpeg(huff_encoded,previous_image,Q)

if (nargin<3)
  Q=80;
end

% decode the Huffman encoded jpeg coefficients
huff_decoded = Huff06( double(huff_encoded) );
dc_coeffs = reshape(huff_decoded{1}, size(previous_image)/8);
ac_coeffs = reshape(huff_decoded{2}, [ 63 prod(size(previous_image)/8)]);

% by default new output image is old (plus any changes made later)
new_image = previous_image;

%-----------change code from here --------------------------------

tile_num=0;
% ANALYSE (AND COMPRESS?) EACH 8x8 BLOCK IN THE IMAGE IN TURN
% FOR LOOPS
for row = 1:8:size(new_image,1)
  for column = 1:8:size(new_image,2)
    tile_num  = tile_num + 1;

      % we have to retrieve the coefficients of the current block
      % to reconstruct the image block


      % 1. retrieve ac coefficients for the current block
      % tile_num would be the index for the ac_coeffs block
      ac_current_coefficients   = ac_coeffs(:, tile_num);

      % 2. retrieve dc coefficients for the current block
      % we need to shift the block to reference the bottom right corner for
      % the dc coefficient
      dc_current_coefficients   = dc_coeffs((row+7)/8, (column+7)/8);

      % 3. determine if block needs updating / decoding
      if (dc_current_coefficients ~= 0 || any(ac_current_coefficients))
      %   NOTE - any block not encoded will have all of the
      %   ac and dc coefficients set to ZERO. This 'clue' can be used to
      %   determine if a image block needs updating here.
      % 4. extract out the decompressed tile (if required)
        decoded_block                         = djpeg_8x8(dc_current_coefficients, ac_current_coefficients, Q)
        new_image(row:row+7, column:column+7) = decoded_block;
      end
    end
end
%
% SEE SIMPLE_MPEG for clues.

%-----------change code above here --------------------------------

% enforce uint8 format
new_image = uint8(new_image);

return

end

% -------------------------------------------------------------------------
