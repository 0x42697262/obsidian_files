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
B       = conv2(I, ones(N) / N^2, 'same');

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

% Compute x and y gradients using Sobel filters
Gradientx = conv2(I, Sobelx, 'same');
Gradienty = conv2(I, Sobely, 'same');

% Compute gradient magnitude and direction
gradient_vector = sqrt(Gradientx.^2 + Gradienty.^2);

% Compute the gradient image G
G = 7 * gradient_vector + 1;

% Compute the weighting function W
W = ones(size(I));

% For each pixel, construct the output image as a weighted combination of the
% blurred and original images using the computed weight values
for r = 1:size(I, 1)
    for c = 1:size(I, 2)
        if gradient_vector(r, c) <= tolerance
            W(r, c) = G(r, c) / tolerance;
        end
    end
end

% Compute the output image as a weighted combination of blurred and original images
out_img = W .* B + (1 - W) .* I;
im2double(out_img);

% ------ INSERT YOUR CODE ABOVE ------

return
end
