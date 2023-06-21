% IMAGE_THRESH - estimate a suitable image threshold value using isothresh
%
function T = hand_threshold(I)

if (isa(I,'uint8'))
  I=double(I)/255;
end


% TO BE FILLED IN BY YOU (See assignment sheet)
% this should implement isothresh for at least 10 iterations. I
% suggest you use the mean of the whole image as the initial value for
% T.

% ---------- INSERT YOUR CODE BELOW ------------------------------------


% average of overall elements

initial_threshold   = mean(I, 'all')

% iterate it at least 10 times. randomly chose 35, no reason at all.

for i = 1:35
  average_intensity_above   = mean(I > initial_threshold, 'all');
  average_intensity_below   = mean(I <= initial_threshold, 'all');

  initial_threshold   = (average_intensity_above + average_intensity_below) / 2;
end

T   = initial_threshold;






% ---------- INSERT YOUR CODE ABOVE ------------------------------------

% END FO FILE
    


