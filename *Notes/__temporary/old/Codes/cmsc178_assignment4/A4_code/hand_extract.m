% HAND_EXTRACT - auto extract the "hand" region of interest from the training
%   image using thresholding, morphological cleaning etc.
%
%  B = hand_extract(I);
%
% I = an NxM gresyscale image (values range 0..1)
% B = Binary mask of extracted region

function B = hand_extract(I)

if (nargin<1)
  error('This function requires an image as input');
end
if (isa(I,'uint8'))
  I = double(I(:,:,1))/255;
end

% estimate a threshold using the isothresh function you have created.
threshold = hand_threshold(I); 

% 1. Threshold the image based on the isothresh estimate. Given that the
%    hand contains significant shadowing uou may need to scale up/down the
%    threshold estimate given by image_thresh(). 
%
% 2. Clean up the thresholded image. Remove isolated points, fill holes
%    in the etc... You can use any of the function in the image processing
%    toolbox to do this such as imerode,imdilate,imopen,imclose,imfill etc.
%    Make sure you test this on serval images from the dataset to be sure it works.
%    Again shadowing across the hand is likely to be an issue.
%
% 3. Return a binary image containing only the "hand", preferably as a single region. 
%    If you have multiple regions in the output (caused by fragmentation of the hand or
%    from noise not removed during the clean up stage) some of the feature estimation 
%    functions which you will use later on may return odd results. 
%
% IMPORTANT - the better this section is at cleaning up the imagery the better the 
% feature estimates are likely to be and hence the performance of the classifier. Also
% make sure you discuss how you came up with these steps in your report and include
% examples etc.
% ----------- FILL IN THE SECTION BELOW ------------------------------


% We must pick images that are only white and black so we will set the threshold value
% for it. 
% B = imbinarize(I, threshold*0.16);
B = imbinarize(I, threshold*0.2625);
% Fill up the holes albeit this function actually never fills up a huge hole gap
B = imfill(B, 'holes'); % Fill holes in the image
% We will use this for the morphological filter
S = strel('disk', 6); 
% Do an erosion and dilation. Remove unwanted pixels and bring the image back to the original shape
B = imopen(B, S); 
% Only keep the biggest shape in the image. We don't have the background to be part of our test.
B = bwareafilt(B, 1);

% Then finally, label the shape to only use. This assigns a unique label to it.
[L, n] = bwlabel(B);
ObjectIdx = 1;
if n ~= 1
    ObjectIdx = mode(L(L>0));
end

% Return the object image
B = L == ObjectIdx;

% ----------- FILL IN THE SECTION ABOVE ------------------------------

return

% -------------------------------------------------------------------
% END OF FILE



