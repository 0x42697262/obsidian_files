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
      % 1. retrieve coefficients for this block
      % 2. retrieve coefficients for this block
      % 3. determine if block needs updating / decoding
      %   NOTE - any block not encoded will have all of the
      %   ac and dc coefficients set to ZERO. This 'clue' can be used to
      %   determine if a image block needs updating here.
      % 4. extract out the decompressed tile (if required)
%
% SEE SIMPLE_MPEG for clues.

%-----------change code above here --------------------------------

% enforce uint8 format
new_image = uint8(new_image);

return

end

% -------------------------------------------------------------------------



  

