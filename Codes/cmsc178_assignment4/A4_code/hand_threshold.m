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
value   = 100;


% iterate it at least 10 times. randomly chose 35, no reason at all.

for i = 1:value
  average_intensity_above   = mean(I > initial_threshold, 'all');
  average_intensity_below   = mean(I <= initial_threshold, 'all');

  initial_threshold   = (average_intensity_above + average_intensity_below) / 2;
end


% Hint: Applying a small scale offset to the threshold estimated by isothresh (eg. “thresh_used = k
% * thresh_est;” may help to reduce problems with shadows seen in the palm of the hand for the
% “scissors” images.

k   = 0.95;

T   = initial_threshold * k;






% ---------- INSERT YOUR CODE ABOVE ------------------------------------

% END FO FILE
    

%%%
%
% So, using a 100% threshold leads to issues like from image 31 on scissors. Even using 90% have issues.
% I tried 50%, I think it worked? Well, it has artefacts that we should not have... 70% doesn't almost
% have any artefacts but there are still some on the wrist. On 85%, we go back to our main issue.
% On 80%, there is an issue somewhere on image 176 or 177. There is a bad scissor on image 177 for 75%.
% I think I should use 70% Threshold value.
% Looking at it again, the rock have artefacts and considering the amount of bad scissors and rocks,
% there are more rocks with artefacts than with scissors. Thus, it's better to stick with 100% scaling threshold.
%
%%%

