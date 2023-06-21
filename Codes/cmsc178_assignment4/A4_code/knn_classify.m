% Function knn_classify
%
% Usage: [c,votes] = knn_classify(f,F,C,n,k);
%
%        f - feature vector
%        F - array of training feature vectors
%        C - vector of class vlaues for each training vector in F
%        n - number of class types in data
%        k - number of nearest neighbours to use to estimate object class
%
% output:
%
%        c - class number of majority of closest matches
%        votes - number of votes of each class

function [c,votes] = knn_classify(f,F,C,n,k)

% duplicate the input feature
ff=meshgrid(f,1:size(F,1));

% compute eulcidean distance
d = sum( (ff-F).^2 , 2 );

% sort by distance
[dsort,dix] = sort(d);

% collate the class of each of the K nearest points
votes=hist( C(dix(1:k)),1:n);

% return class number with the most votes
[mx,c] = max(votes); 

return




