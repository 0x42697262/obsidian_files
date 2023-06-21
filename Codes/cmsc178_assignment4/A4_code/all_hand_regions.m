% hand_regions(mode) - test script to region extract hand images. This
% function does nothing but display the processing of the region extractor.
%
% The subdirectories 'rock' 'paper' 'scissors' 
% should be present. 
%

function hand_regions

% NOTE: do not alter this code

cname = { 'rock' 'paper' 'scissors' }; % run 3 classes
  

%figure(2345); clf;
for classnum=1:length(cname)
  D=dir([ cname{classnum} filesep '*.png']);
  if (isempty(D)); error('Unable to find the required image directory: please make sure the data directories are present'); end
  for n=1:length(D)
    % load rock/paper/scissors/etc image
    disp(['Loading ' D(n).name]);
    I = imread([ cname{classnum} filesep D(n).name]);
    I = double(I(:,:,1))/(1+isa(I,'uint8')*254);
    
    % Here is the calls to the region (HAND) extraction step
    B = hand_extract(I);

    % diplay diagnostics
    figure(1234);
    % raw image
    subplot(1,2,1); imagesc(I); axis equal tight;
    title( [ D(n).name ' (class ' num2str(classnum) ')' ] , 'interpreter' , 'none' );
    % mask region
    subplot(1,2,2); imagesc(B); axis equal tight;
    title('Extracted Hand Shape');
    
    colormap(gray);
    drawnow;
    
    %disp('Press a key...');
    %pause
  end
end

% ------------------------------------------------


