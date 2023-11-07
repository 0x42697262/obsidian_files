% MEDIAN_FILTER
%
% Usage:
%         med_img = median_filter(img,M,N)
%
% M,N size of MxN median filter to employ. 

function med_img = median_filter(img,M,N)

% ensure img is 0..1 and greyscale
img = im2double(img);
if (size(img,3)==3)
  img=rgb2gray(img);
end

% ----- INSERT YOUR OWN CODE BELOW -----

% Hint: the simplest solution is to use for loops and the sort() function
% to solve this. Consider also how you plan to deal with values near the
% boundary.

% Early return if MxN is < 2.
if M < 2 && N < 2
  med_img   = img;
  return
end

% Pad the image near the boundary
padded_img  = padarray(img, [floor(M/2) floor(N/2)], 'symmetric');

% Create output image with the same size of the input filled with zeros
med_img     = zeros(size(img));

% Iterate over each pixel in the input image
for row = 1:size(img, 1)
  for column = 1:size(img, 2)
    % Define the range of pixels to be used for the median filtering operation
    entire_row      = row:row+M-1;
    entire_column   = column:column+N-1;

    % Extract the pixels within the defined range
    pixels          = padded_img(entire_row, entire_column);

    % Sort the extracted pixels in ascending order
    sorted_pixels   = sort(pixels(:));
    
    % Compute the median value and assign it to the corresponding pixel in
    % the output image
    if mod(M*N, 2) == 0
      med_img(row, column)  = mean(sorted_pixels(M*N/2:M*N/2+1));
    else
      med_img(row, column)  = sorted_pixels((M*N+1)/2);
    end

  end
end


% ----- INSERT YOUR OWN CODE ABOVE -----

return
end




