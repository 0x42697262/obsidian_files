% HAND_FEATURES - extract shape features for the supplied region of
%  interest suitable for classification.
%
% F = hand_features(B)
% 
% B = binary image mask
%
% F - an 1xN row-vector of feature measurement (real numbers)

function F = hand_features(B)

% Extract features related to shape. Make use of the concepts covered
% in the lectures. MATLAB has a number of useful pre-existing feature 
% measures to try out but I suggest you also create some of your own
% if you wish to get good results.

% ---------- INSERT YOUR CODE BELOW ------------------------------------

% DELETE THIS LINE - IT JUST GENERATES A 1x5 vector OF DUMMY DATA
F = [5 4 3 2 1] .* randn(1,5) + [1 2 3 4 5];

% ---------- INSERT YOUR CODE ABOVE ------------------------------------

return

% END OF FILE
