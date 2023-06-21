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
     
T = rand(1,1); % <--- DELETE and REPLACE

% ---------- INSERT YOUR CODE ABOVE ------------------------------------

% END FO FILE
    


