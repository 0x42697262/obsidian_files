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

B = rand(size(I,2),size(I,2)); % dummy result, remove this line

% ------ INSERT YOUR CODE ABOVE ------

return
end

