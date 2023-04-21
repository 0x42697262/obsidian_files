% APPLY_RGB_MAP - replace R,G and B values in an image based
%  on the supplied lookup table
%
% Usage:
%          adjusted_image = apply_rgb_map(img,map)
%
% img -  NxMx3 uint8 image
% map -  256x3 lookup table for R,G,B values in range 0..255
%
% note R,G and B values are mapped independently. The RGB triples
% do not represent actual colours in the image (this is not a colormap).

function adjusted_image = apply_rgb_map(RGB_image,RGB_map)

% remap each RGB value in the current image onto a new image. Remember
% to treat each RGB channel separately. Also entry 1 in the table is
% colorlevel 0 and entry 256 is colorlevel 255

% ----- ADD YOUR CODE BELOW -----

% Initialize zeros list for the corrected image
adjusted_image  = zeros(size(RGB_image));

for row = 1:size(RGB_image, 1)
  for column = 1:size(RGB_image, 2)
    % adjusted_image(row, column, :) = RGB_map(RGB_image(row, column, :) + 1, :);
    adjusted_image(row, column, 1) = RGB_map(RGB_image(row, column, 1) + 1, 1);
    adjusted_image(row, column, 2) = RGB_map(RGB_image(row, column, 2) + 1, 2);
    adjusted_image(row, column, 3) = RGB_map(RGB_image(row, column, 3) + 1, 3);
  end
end


% ----- ADD YOUR CODE ABOVE -----

% resulting image must be uint8 with values in range 0..255
adjusted_image = uint8(adjusted_image);
return

end
