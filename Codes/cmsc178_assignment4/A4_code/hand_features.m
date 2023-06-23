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

% Get features using regionprops
% uncomment the ones that we don't need. append the ones we need
feats   = {};
feats{end+1} = 'Circularity';
feats{end+1} = 'Perimeter';
feats{end+1} = 'Area';
feats{end+1} = 'Solidity';
feats{end+1} = 'MajorAxisLength';
feats{end+1} = 'MinorAxisLength';
features = regionprops(B, feats, 'table');

PerimeterAreaRatio = features.Perimeter / features.Area;
Roundness = features.MajorAxisLength / features.MinorAxisLength;


F = [features.Solidity Roundness PerimeterAreaRatio];

% ---------- INSERT YOUR CODE ABOVE ------------------------------------

return

% END OF FILE
