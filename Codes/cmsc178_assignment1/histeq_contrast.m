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

% ----- INSERT YOUR CODE BELOW -----
img               = uint8(img * 255);

% Compute the histogram of the input image using the histogram() function
% only purpose is to display the histogram of the image input
histogram_img     = histogram(img(:), 0:255);

% Extract the frequency counts from the histogram object
histogram_result  = histcounts(img(:), 0:255);

% Calculate the cumulative distribution function (CDF)
cdf               = cumsum(histogram_result);

% Calculate the equalization map
equalization_map  = uint8((cdf / max(cdf)) * 255);

% Replace the original pixel values with the equalized values using the lookup table
new_img           = equalization_map(img + 1);

% Convert the image back to a double in the range 0.0 to 1.0
eq_img            = double(new_img) / 255;

% ----- INSERT YOUR CODE ABOVE -----

return
