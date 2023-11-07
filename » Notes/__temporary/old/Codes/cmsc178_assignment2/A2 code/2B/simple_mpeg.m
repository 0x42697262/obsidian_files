%
% A SIMPLE MPEG LIKE ENCODING OF SEQUENTIAL IMAGERY
%
% current_image - current uint8 image to encode
% reference_image - image to compare to to determine which 8x8 regions need
%                   updating. If empty then encode the entire image.
% Q - quality factor to employ in compression
%
% huff_encoded - Huffman encoded data (created by Huff06.m)
% updated_reference - updated reference image.
%

function [huff_encoded,updated_reference] = simple_mpeg(current_image,reference_image,Q,diff_tolerance)

if (nargin<3)
  Q=80;
end
if (nargin<4)
  diff_tolerance=1;
end

debugprint=false; % <--- useful check for which blocks are blanked.

% Note whether we need to compress the full image or just the blocks
% containing significant differences
fullframe = isempty(reference_image) || (diff_tolerance < 0);
if (fullframe)
  updated_reference = current_image;
else
  updated_reference = reference_image;
end

% variables used to store quantised dc and ac coefficients prior to huffman
% encoding
dc_coeffs = zeros(size(current_image)/8);
ac_coeffs = zeros(63,prod(size(current_image)/8));

tile_num=0;
% ANALYSE (AND COMPRESS?) EACH 8x8 BLOCK IN THE IMAGE IN TURN
for ii = 1:8:size(current_image,1)
    for jj = 1:8:size(current_image,2)
      % extract the 8x8 region to be encoded?
      tile = current_image(ii:ii+7, jj:jj+7);
      tile_num = tile_num+1;
      % determine if the 8x8 block needs compressing
      if (~fullframe)
        % same region from reference image (to compare with)
        ref_tile = reference_image(ii:ii+7, jj:jj+7);
        % determine if this block needs updating and encoding
        update_block = update_check(tile,ref_tile,diff_tolerance);
        
      else
        % full frame mode, update all areas
        update_block= true;
      end
      
      if (update_block)
        % ensure returned reference image contains encoded block
        updated_reference(ii:ii+7, jj:jj+7) = tile;
        % CALL 8x8 JPEG function
        [dc_iijj,ac_iijj] = jpeg_8x8( tile , Q );
        % record coefficients for this block
        dc_coeffs((ii+7)/8, (jj+7)/8)= dc_iijj;
        ac_coeffs(:,tile_num) = ac_iijj;
        
        % NOTE - any block not encoded by the above will have all of the
        % ac and dc coefficients set to ZERO. This 'clue' will be used in
        % the DMPEG step to identify blocks which match the old data.
        
      else
        % do nothing
        if (debugprint)
          fprintf(1,'blanked %d %d\n',ii,jj);
        end
      end
    end
end

% Huffman encode the quantised coefficients (you do not need to
% understand how Huff06() works we just use it!)
huff_encoded = uint8( Huff06( { dc_coeffs(:) ac_coeffs(:) } ,1 , 0) );

return

end

% ----------------------------
% UPDATE_CHECK - true if mean square error exceeds given tolerance

function update_block = update_check(tile,ref_tile,tolerance)
mse= sqrt(sum(sum( (double(tile)-double(ref_tile)).^2 ))/64);
update_block = (mse > tolerance);
end




  

