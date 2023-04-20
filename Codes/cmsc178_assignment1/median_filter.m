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

% create dummy image
med_img=rand(size(img));

% Hint: the simplest solution is to use for loops and the sort() function
% to solve this. Consider also how you plan to deal with values near the
% boundary.


% ----- INSERT YOUR OWN CODE ABOVE -----

return
end




