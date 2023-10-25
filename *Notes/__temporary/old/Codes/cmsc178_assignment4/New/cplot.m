% CPLOT2 plot feature vs class as histograms, image or scatterplot.
%	CPLOT2(x,c)
%
%  The type of display layoput is dependant on the data dimensions and
%  parameters:
%
%    CPLOT(x,c)   - histogram plots               ( if X is 1-D )
%    CPLOT(x,c)   - 2D scatterplot (X is Nx2)
%    CPLOT(x,c)   - 3D scatterplot (X is Nx3, Nx4 or higher)
%    CPLOT(x,c,'sorted')
%
% In the case that X has 4 or more columns, PCA is used to estimate
% the 3 most significiant eigenvectors and a 3D scatterplot of this
% is produced.
%
%  Author: 	Danny Gibbins
%
% PLEASE NOTE THIS IS A USEFUL FUNCTION FOR GENERATING SCATTER PLOTS OF
% YOUR FEATURE DATA TO SEE IF YOU HAVE GOT SEPARATION BETWEEN CLASSES. 
% FOR FEATURE DATA OF 4 OR MORE DIMENSIONS IT USES A SIMPLE VERION
% OF  PCATO REPORJECT THE DOMINANT 3 EIGENVECTORS AND GIVES YOU A 3D
% PLOT. IF YOU CANS EE SEPARATION HERE THEN IT MEANS YOU SHOULD ALSO HAVE 
% GOOD SEPARATION IN THE HIGHER DIMENSIONS. - DG.
%
% PPS: ITS AN OLD PIECE OF CODE.
%


function cplot(X,C,mode,key)


colr_list = [ 1 0 0 ; 0 1 0 ; 0 0 1 ; 1 1 0 ; 1 0 1 ; 0 1 1 ; 0 0 0 ; ...
	0.5 0.5 0.5 ; 0.9 0.6 0 ; 0.6 0 0.9 ; 0 0.9 0.6 ];

point_list= 'x+osdv^><ph*';

if (nargin<4)
  key=[];
end
if (nargin<3)
  mode='scatter';
elseif (isempty(mode))
  mode='scatter';
end
if (nargin < 2)
	disp('function needs at least 2 arguments.');
	return;
end
if (size(C,1)==1); C=C';end
if (size(X,1) ~= length(C) )
	disp('X and C crray size mismatch.');
	return
end

if (any(isnan(X(:))|isinf(X(:))))
	ix = find ( all( ~isnan(X) , 2 ) & all( ~isinf(X) , 2 ) );
	if (isempty(ix))
		disp('Matrix X contains no entries excluding NaN/Inf values.');
		return;
	else
		disp('warning: NaN/Inf values detected in data, deleting...');
	end
	X=X(ix,:);
	C=C(ix);
end
		
clist = sort(unique(C))';
if (length(clist) > 999)
	disp('cplot: too many classes, may be a legacy code call, aborting plot.');
	return
end

if ( strcmp(mode,'sorted') )
  % display as sorted lists of feature vectors
  %
  Ivec=zeros(size(X));
  n=0;
  ends=[];
  for c=clist
    Xc=sortrows( X(C==c,:) );
    Ivec((n+1):n+size(Xc,1),:)=Xc;
    n=n+size(Xc,1);
    ends(end+1)=n;
  end
  hold off; cla reset;
  imagesc(Ivec); 
  colorbar;
  hold on
  for i=1:length(ends)
    hh=plot([0.5 size(X,2)+0.5],[ends(i) ends(i)],'w:');
    set(hh,'linewidth',1.5)
  end
  hold off
  colormap(hot);
  xlabel('Features');
  ylabel('Class Groups');
  title('Feature Vectors -  Sorted and grouped by class');
  set(gca,'YTick',(ends+[0 ends(1:(end-1))])/2);
  set(gca,'YTickLabel',num2str(clist','C%1d'));
  drawnow
  
else
  % MODE - scatterplot (or histogram-like if 1D data)
  switch (size(X,2))
    case 1
      %
      % HISTOGRAM PLOTS
      %
      hold off; cla reset;
      xrng = min(X):((max(X)-min(X))/64):max(X);
      colr=1;
      for c=clist
        hdata = hist(X(C==c),xrng);
        hdata = 0.8*hdata/max(max(hdata),1);
        hold on
        h=plot(xrng,hdata+c,'-');
        %      h=stairs(xrng,hdata+c,'-');
        set(h,'Color',colr_list(colr,:)/1.5);
        colr=rem(colr,11)+1;
      end
      colr=1;
      yticks = [];
      yticklabels = {};
      for c=clist
        indx = find(c==C);
        h=plot(X(indx),C(indx),'x');
        set(h,'Color',colr_list(colr,:));
        yticks = [ yticks c+0.5 ];
        %yticklabels = { yticklabels{:} [ 'C' num2str(c) ] };
        colr=rem(colr,11)+1;
      end
      yticklabels = set_legend(clist,key);
      set(gca,'YTick',yticks);
      set(gca,'YTickLabel',yticklabels);
      title('Feature Vs Class');
      xlabel('Feature');
      ylabel('Class');
      hold off;
      % ------------------------------------------------------------------
    case 2
      %
      % 2D SCATTER PLOTS
      %
      hold off; cla reset;
      colr = 1;
      pstyle=1;
      lstring = {};
      for i=clist
        indx = find(C==i);
        h=plot(X(indx,1),X(indx,2),point_list(pstyle));
        set(h,'Color',colr_list(colr,:));
        hold on;
        colr=rem(colr,11)+1;
        pstyle=rem(pstyle,12)+1;
      end
      lstring = set_legend(clist,key);
      legend( char(lstring) );
      hold off;
      title('2D Scattern Plot');
      xlabel('Feature 1');
      ylabel('Feature 2');
      hold off;
      % ------------------------------------------------------------------
    case 3
      %
      % 3D Scatterplot
      %
      plottitle='3D Scattern Plot';
      hold off; cla reset;
      colr = 1;
      pstyle=1;
      lstring = {};
      for i=clist
        indx = find(C==i);
        h=plot3(X(indx,1),X(indx,2),X(indx,3),point_list(pstyle));
        set(h,'Color',colr_list(colr,:));
        hold on;
        colr=rem(colr,11)+1;
        pstyle=rem(pstyle,12)+1;
      end
      lstring = set_legend(clist,key);
      legend( char(lstring) );
      hold off;
      title(plottitle);
      xlabel('Feature 1');
      ylabel('Feature 2');
      zlabel('Feature 3');
      grid on;
      axis square;
      hold off
      % ------------------------------------------------------------------
    otherwise
      %
      % LDA projection of higher dimension scatter plot in 3D
      %
      disp('warning: There are more than 3 plot feateures, applying PCA...');
      plottitle='3D Scattern Plot (PCA projection)';

      %[E,t]=lda_matrix(X,C); fr = 'MDA';
      [E,e]=dopca( cov(X) ,3); fr = 'PCA';

      Xp(:,1) = X*E(:,1);
      Xp(:,2) = X*E(:,2);
      Xp(:,3) = X*E(:,3);
      hold off; cla reset;
      colr = 1;
      pstyle=1;
      lstring = {};
      for i=clist
        indx = find(C==i);
        h=plot3(Xp(indx,1),Xp(indx,2),Xp(indx,3),point_list(pstyle));
        set(h,'Color',colr_list(colr,:));
        hold on;
        colr=rem(colr,11)+1;
        pstyle=rem(pstyle,12)+1;
      end
      lstring = set_legend(clist,key);
      legend( char(lstring) );
      hold off;
      title(plottitle);
      xlabel([fr ' eig1']);
      ylabel([fr ' eig2']);
      zlabel([fr ' eig3']);
      grid on;
      axis square;
      hold off
  end
  
end % mode test

hold off;

return

% -------------------------------------------------------------------------

function lstring = set_legend(clist,key)

lstring={};
if (isempty(key))
  for i=clist
    lstring = { lstring{:} [ 'C' num2str(i) ] };
  end
elseif ~iscell(key)
  for i=clist
    ix = find(key.value==i);
    if (~isempty(ix))
      lstring = { lstring{:} key.labels{ix(1)} };
    else
      lstring = { lstring{:} [ 'C' num2str(i) ] };
    end
  end
else
  lstring = key;
end
return

% ----------------------------------------------------------------------------

% function [Pz, lambdaZ] = dolda(C,M,M0,VNC)
% 
% Calculates the tranformation matrix for LDA/MDA. 
%
% C   : 3D matrix containing covariance matrices for each class 
%       e.g. C(:,:,1) references the covariance matrix for class 1
%       If size(C,1) is less than size(C,3) then an empty matrix is
%       returned.
%       Assumes unbiased estimate of covariance matrices.
% M   : Matrix containing mean vectors. e.g. M(:,1) is mean vector
%       for class 1
% M0  : expected vector of the overall distribution of the feature data 
%       used to generate C and M
% VNC : Vector with element NC(C) the number of vectors in class C
% 
% Pz  : Tranformation matrix for LDA/MDA
% lambdatX : Eigendvalues used in determining Pz composition.
%
% Uses the algorithms in:
% K. Fukunaga, Introduction to Statistical Pattern Recognition, 2nd Ed,
% New York, Academic Press, 1990.

% Author: S.Slomka
% Created on : 29/3/99

function [Pz, lambdaZ] = dolda(C,M,M0,VNC)


Nc =size(C,3); % Number of speaker classes
Pz=[];
lambdaZ=[];

maxval=1;
% check for all zeros in a class covariance matrix
for i=1:Nc
  if( (max(max(C(:,:,i))) == 0) & (max(M(:,i)) == 0) )
    maxval=0
  end
end

if( (size(C,1) >= Nc) & maxval) 
  % Find the within-class scatter matrix
  total=zeros(size(C(:,:,1)));
  for i=1:Nc
    total=total+((VNC(i)-1)*C(:,:,i));   % equiv to Prior(i)*covmatrix(i)
  end
  Sw = total;     
  
  % Find the between-class scatter matrix
  total=zeros(size(C(:,:,1)));
  for i=1:Nc
    temp=M(:,i)-M0; 
    total=total+(VNC(i)*temp*temp');
  end
  Sb = total;    
  
  if(rank(Sw)==size(Sw,1))
    % Now find the eigenvectors and eigenvalues of the transformation matrix
    W = inv(Sw)*Sb;
  else
    % Now find the eigenvectors and eigenvalues of the transformation matrix
    disp('Within-class scatter matrix close to singular using pseudo inverse');
    W = pinv(Sw)*Sb;
  end
  [Pz, lambdaZ] = dopca(W,(Nc-1));
  
else
  if(maxval)
    disp('Dimensionality of input features is already less than the number of classes');
  else
    disp('Missing training data for one or more classes');
  end
  disp('Returning Pz = lambdaZ = []');
end

% function [Pz, lambdaZ] = dopca(C,t);
%
% Extract the t most significant eigenvectors corresponding to the largest
% eigenvalues for covariance matrix C. These become the PCA tranfromation
% matrix. Eigenvectors are in column form. 
%
% Pz  	: Tranformation matrix for LDA/MDA 
% lambdatX : Eigendvalues used in determining Pz composition.
%
% C   	: Covariance matrix
%
% Author:  S.Slomka
% Created on: 29/3/99

function [Pz, lambdaZ] = dopca(C,t)

% Get eigenvectors and eigenvalues
[Q, q] = eig(C);

% Extract t most significant eigenvectors
Pz = [];  
q2 = diag(q);
[lambdaZ(:,1), index] = sort(q2);  % ascending order
N = length(q2);
k=1;

for i=N:-1:N-t+1
  Pz(:,k) = Q(:,index(i));
  k=k+1;
end
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     

% LDA_MATRIX compute LDA/MDA transform matrix for given feature data
%	[T,lambda] = LDA_MATRIX(feats,classnumbers,<flag>)
%
% feats       : (NxM) matrix of feature values
% classnumbers: (Nx1) class number of each feature vector

% ---------------------------------------------------------------------------
%
%      Title: 	compute LDA/MDA transform matrix for given feature data
%    Created: 	Tue Sep 26 11:51:19 2000
%     Author: 	Danny Gibbins
%		Centre for Sensor Signal and Information Processing (CSSIP)
%		Signal Processing Research Institute
%		Technology Park, S.A.
%
%		<danny@cardrona.cssip.edu.au>
%
%      Notes: 	
%
%        RCS: $Id$
%
%
% ---------------------------------------------------------------------------

function [T,lambda] = lda_matrix(feats,classnums,flag)


if (nargin < 3)
  flag=0;
end

classlist= unique(classnums);
classes  = length(classlist); %  number of classes observed 

C   = zeros(size(feats,2),size(feats,2),classes);
M   = zeros(size(feats,2),classes);
M0  = zeros(size(feats,2),1);
VNC = zeros(classes,1);

for c=1:classes;
  indx = find(classnums==classlist(c));
  if ( ~isempty(indx) )
    if (flag)
      VNC(c) = 999; % remove "priors" bias
    else
      VNC(c)   = length(indx);
    end
    M(:,c)   = mean(feats(indx,:),1)';
    if ( length(indx) > 1)
      C(:,:,c) = cov(feats(indx,:));
    end
  end  
end

M0 = mean(feats,1)';

% ----------------------------------------------------------------------------

[T,lambda] = dolda(C,M,M0,VNC);

if (isempty(T))
  T = eye(size(feats,2));
end

% ----------------------------------------------------------------------------




