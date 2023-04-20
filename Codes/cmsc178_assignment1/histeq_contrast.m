% HISTEQ_CONTRAST - histogram equalisation for contrast enhancement
%
% Usage:
%         eq_img = histeq_contrast(img)
%
%  input image data is assumed to be in range 0..1

function eq_img = histeq_contrast(img)

% ----- INSERT YOUR CODE BELOW -----

% OPTIONAL HINT to make it easier to index you can multiply the img 
%   values by 255 and use a 256 element histogram.

% REPLACE THIS LINE OF CODE
eq_img = rand(size(img)); % <--- return dummy result for now

% ----- INSERT YOUR CODE ABOVE -----

return