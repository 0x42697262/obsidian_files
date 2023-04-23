% SMART_BLUR - blur image to remove noise, but attempt to preserve
%  edge details where possible
%
% USAGE:
%   image_out = smart_blut( image_in , N , tolderance )
%
%    N         - size of NxN blur to apply to data (def. 5).
%    tolerance - estimate of gradient based on noise alone. Used to
%                contol weighting between oriignal and smoothed data
%                returned by function (def. 0.015)
%
% NOTE: all image data is converted to greyscale, with values in range 
%      0.0..1.0 before filtering is applied.

function B = smart_blur(I,N,tolerance)

% convert to greyscale 0.0..1.0
I =im2double(I);
if (size(I,3)==3)
  I=rgb2gray(I);
end

% handle missing input parameters
if (nargin<2)
  N=5;
  if (nargin<3)
    tolerance=0.015; % about 4 greylevels for 8bit data
  end
  if (nargin<1)
    error('This function requires an image as input');
  end
end

% ------ INSERT YOUR CODE BELOW ------
% Create a blurred image B using a simple NxN averaging filter
blurred_image   = conv2(I, ones(N) / N^2, 'same');

% Calculate the x and y image gradients using the following 5x5 sobel
% filter.
Sobelx  = [ -4,   -5,   0,    5,    4; 
            -8,   -10,  0,    10,   8;
            -10,  -20,  0,    20,   10;
            -8,   -10,  0,    10,   8; 
            -4,   -5,   0,    5,    4];
Sobely  = [ 4,    8,    10,   8,    4; 
            5,    10,   20,   10,   5;
            0,    0,    0,    0,    0;
            -5,   -10,  -20,  -10,  -5; 
            -4,   -8,   -10,  -8,   -4];
Sobelx      = Sobelx*(1/240);
Sobely      = Sobely*(1/240);

padded_image    = padarray(blurred_image, [2,2], 'replicate', 'both');

[row, column]   = size(padded_image);


for r = 3:row - 2
  for j = 3:column - 2
    pixels      = padded_image(r-2 : r+2, j-2 : j+2);

    Gradientx(r, j)   = (pixels(r,j) * Sobelx(r,j));
    Gradienty(r, j)   = (pixels(r,j) * Sobely(r,j));

    Gradientx(r, j)   = (pixels(r,j) * Sobelx(r,j));
    Gradienty(r, j)   = (pixels(r,j) * Sobely(r,j));
  end
end


% ------ INSERT YOUR CODE ABOVE ------

return
end

