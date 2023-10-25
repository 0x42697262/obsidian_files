% ALL_HAND_CLASSIFY - split up the hand feature data and classify one part using the
%  data from the other and a KNN classifier.
%
% Here: F is the array of feature vectors
%       C is the vector of class values for each vector (eg. 1,2 3 etc)
%       k is the number of nearest neighbours to use
%

function [C_est,C_true] = all_hand_classify(F,C,k)

train_fraction = 0.5;

figure(4321); clf;
subplot(2,3,[1 2 4 5]);
colr='rgbmyck';
symb='x+o*sdv';
classstr = { 'rock' 'paper' 'scissors' };
yesnostr = { 'INCORRECT' 'CORRECT' };


if (nargin<3)
  disp('warning: you have not specified k, assuming k=3');
  k=3;
end

%
% part 1 - split data into a train and test set (default 50:50)
%
disp('Splitting Data into test and train components...')
Ctrain=[];
Ctest=[];
IXtest=[];
Ftrain=[];
Ftest=[];
classlist=unique(C); nclasses=max(C);
for class=1:length(classlist)
  ix=find(C==classlist(class));
  if (~isempty(ix))
    % split train and test into two
    mid=ceil(length(ix)*train_fraction);
    ixlo=ix(1:mid);
    ixhi=ix((mid+1):end);
    
    % append ixlo to train
    Ctrain(end+[1:length(ixlo)])=C(ixlo);
    Ftrain(end+[1:length(ixlo)],:)=F(ixlo,:);

    subplot(3,3,[1 2 4 5]);
    hold on
    plot( F(ixlo,1) , F(ixlo,2) , [ symb(class) colr(class) ] );
    xlabel('F1');ylabel('F2');
    title('Training Data Scatterplot');
    hold off
    
    % append ixhi to test
    Ctest(end+[1:length(ixhi)])=C(ixhi);
    Ftest(end+[1:length(ixhi)],:)=F(ixhi,:);
    IXtest=[ IXtest ixhi' ];
  end
end

drawnow;

%
% part 2 - classify each item in test set using train set
%
hh=[];
for n=1:length(Ctest)
  
  % display stuff
  if (~isempty(hh))
    delete(hh);
  end
  subplot(2,3,3); cla;
  plot(Ftest(n,:),'bo:');
  a=axis; axis( [0.5 size(Ftest,2)+0.5 a(3) a(4) ] );
  xlabel('Feature Number');
  ylabel('Feature Value');
  title( [ 'Test Vector (entry ' num2str(n) ')' ] );
  
  subplot(3,3,[1 2 4 5]);
  hold on
  hh=plot(Ftest(n,1),Ftest(n,2),'ks');
  set(hh,'markersize',2*get(hh,'markersize'));
  hold off;
  
  % run the actual classifier
  fprintf(1,'Classifying entry %d (%d): ',n,IXtest(n));
  c = knn_classify(Ftest(n,:),Ftrain,Ctrain,nclasses,k);
  C_est(n)=c;
  C_true(n)=Ctest(n);
  fprintf(1,'%12s ... %s\n',classstr{c},yesnostr{(Ctest(n)==c)+1});
  
  subplot(3,3,[7 8 9]); 
  hold on;
  plot(n,C_true(n),'bx');
  if (C_est(n) == C_true(n) )
    plot(n,C_est(n),'go');
  else
    plot(n,C_est(n),'ro');
  end
  title( sprintf('Classification summary: %d/%d correct',sum(C_est==C_true),length(C_true)) );
  hold off
  drawnow;
  
end

disp('Completed...');
disp('Note: bracketed numbers above refer to entry in original feature dataset.');

return



