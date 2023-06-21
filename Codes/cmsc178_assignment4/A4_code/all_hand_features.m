% [F,C]=all_hand_features(mode) - script to generate array of feature data
%  from the raw hand images. Calls up extract_hand().
%
% the subdirectories 'rock' 'paper' 'scissors'
% should be present. Returns the NxM array of features
% all the loaded imagery, and C is the associated class values.
%

function [F,C] = hand_features

% NOTE: do not alter this code

cname = { 'rock' 'paper' 'scissors' }; % run on just 3 classes

count=0;
figure(1234); clf;
colr='rgbmyck';
symb='x+o*sdv';
for classnum=1:length(cname)
  D=dir([ cname{classnum} filesep '*.png']);
  if (isempty(D)); error('Unable to find the required image directory: please make sure the data directories are present'); end
  for n=1:length(D)
    % load rock/paper/scissors/etc image
    disp(['Loading ' D(n).name]);
    I = imread([ cname{classnum} filesep D(n).name]);
    I = double(I(:,:,1))/(1+isa(I,'uint8')*254);
    
    % Here is the calls to the two key processing functions you
    % need to write
    B = hand_extract(I);
    Fn = hand_features(B);

    % diplay diagnostics
    figure(1234);
    % raw image
    subplot(2,2,1); imagesc(I); 
    title( [ D(n).name ' (class ' num2str(classnum) ')' ] , 'interpreter' , 'none' );
    % mask region
    subplot(2,2,2); imagesc(B); 
    title('Extracted Region');
    % feature vec
    subplot(2,2,3);
    plot(Fn,'bo:');
    a=axis; axis( [0.5 size(Fn,2)+0.5 a(3) a(4) ] );
    xlabel('Feature Number');
    ylabel('Feature Value');
    title('Feature Vector');
    % summary scatter plot of first two features (if present)
    subplot(2,2,4); 
    hold on
    if (size(Fn,2)>=2)
      plot( Fn(:,1), Fn(:,2) , [ symb(classnum) colr(classnum) ] );
    end
    colormap(gray);
    title('Scatterplot'); xlabel('F1'); ylabel('F2');
    drawnow;
    
    % set class and feature vector info
    count=count+1;
    F(count,:)=Fn;
    C(count,1)= classnum;
  end
end

% ------------------------------------------------


