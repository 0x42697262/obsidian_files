% CLASS_SUMMARY generate nice summary plot
%	CLASS_SUMMARY(actclass,classresults<,names><,legacy>)
%
% actclass is a vector. Classresults is a N x C matrix, where C is the number
% of classes. if bwflag is set plot is intended for printing. Names
% is an optional list of classnames ( C x 2 ).
%
% Names can also be a record with at lest two fields named 'labels' and
% 'value'.
%
% Including a value of 1 for the legacy parameter will plor the full
% matrix including any blank classes.
%
% Author: 	Danny Gibbins
%
% THIS IS A USEFUL FUNCTION FOR DISPLAYING A CONFUSION MATRIX OF THE 
% CLASSIFICATION SCORES YOU HAVE OBTAINED. IT SHOWS THE PROPORTION
% OF EACH CLASS AND EACH PREDICTION. IDEALLY YOU WANT 1.0's ALONG
% THE DIAGONAL IE PERFECT SCORE BUT IT IS EXREMELY RARE TO OBTAIN
% IN THE REAL WORLD. -DG.

function psummary = class_summary(act_class,class_predictions,names,legacy_plot)

if (nargin<4)
  legacy_plot=false;
end

blk = 'k';blk2=[0.35 0.35 0.35];
wht = 'w';wht2=[0.65 0.65 0.65];

addunkclass_pred=false;
addunkclass_act=(min(act_class)<=0);
if (size(class_predictions,2)==1)
  disp('Treating Nx1 class prediction array as hard class values...');
  bestc=class_predictions;
  if (min(bestc)<=0)
    bestc(bestc<=0)=max(bestc)+1;
    addunkclass_pred=true;
  end
  class_predictions=zeros(size(bestc,1),max(max(act_class),max(bestc)));
  cp_ix = sub2ind( size( class_predictions ) , [1:size(bestc,1)]' , bestc );
  class_predictions(cp_ix)=1;
end

classes  = size(class_predictions,2 );

if (classes > 35)
  disp('warning: parameter 2 looks wrong, too many columns for classes');
end

if ( nargin < 3 )
	names=cell(1,classes);
	for i=1:classes
		names{i}=sprintf('C%d',i);
	end
elseif (isstruct(names))
  namesrec=names;
  names=cell(1,classes);
  for i=1:classes
    ix=find(namesrec.value == i);
    if (~isempty(ix))
      names{i}=namesrec.labels{ix(1)};
    else
      names{i}=sprintf('C%d',i);
    end
	end
end

% add unknown class if any true class is 0 (ie unknown)
if ( addunkclass_act || addunkclass_pred )
  if (addunkclass_act && (~addunkclass_pred))
    classes=classes+1;
    class_predictions(:,classes)=0;
  end
  act_class(act_class<=0)=classes;
  names{end+1}='UNKNOWN';
end

% clip class names to 14 characters
for i=1:length(names)
  if length(names{i}) > 14
    names{i}=[ names{i}(1:12) '`' names{i}(end) ];
  end
end


psummary = zeros(classes,classes);
csummary = psummary;

for i=1:classes
  ind = find(act_class(:)==i);
  if (~isempty(ind))
    [tmp,cmax]=max(class_predictions(ind,1:classes),[],2);
    psummary(i,1:classes) = sum(class_predictions(ind,1:classes))/length(ind);
    for jj=1:classes
      csummary(i,jj) = sum(cmax==jj);
    end
  end
end

if ( legacy_plot )
  % OLD VERSION
  imagesc(psummary');axis xy;
  colormap(hot);
  pmax = max(max(psummary));
  for i=1:classes
    for j=1:classes
      if (psummary(i,j) > pmax/2); clr=blk;clr2=blk2;else clr=wht;clr2=wht2;end;
      h= text(i,j, sprintf('%4.2f',psummary(i,j)));
      set(h,'HorizontalAlignment','center','Color',clr);
      h2= text(i,j-0.35, sprintf('(%1d)',csummary(i,j)));
      set(h2,'HorizontalAlignment','center','Color',clr2,'Fontsize',get(h2,'Fontsize')*0.7);
    end
  end

  set(gca,'XTick',1:classes);
  set(gca,'XTickLabel',names);
  set(gca,'YTick',1:classes);
  set(gca,'YTickLabel',names);

else
  % NEW RENDERING - REMOVES CLASSES NOT IN PREDICTION OR TRUTH DATA
  nonblank=true(classes,1);
  nonblankr=true(classes,1);
  nonblankc=true(classes,1);
  for i=1:classes
    if (sum(psummary(i,:))==0)&&(sum(psummary(:,i))==0)
      nonblank(i)=false;
    end
    nonblankc(i)= ~(sum(psummary(i,:))==0);
    nonblankr(i)= ~(sum(psummary(:,i))==0);
  end
  imagesc(psummary(nonblankc,nonblankr)');axis xy;
  colormap(hot);
  pmax = max(max(psummary));
  cc=1:classes;
  ccr=cc(nonblankr);
  ccc=cc(nonblankc);
  for i=1:length(ccc) % ccr
    for j=1:length(ccr) % ccc
      if (psummary(ccc(i),ccr(j)) > pmax/2); clr=blk;clr2=blk2;else clr=wht;clr2=wht2;end;
      h= text(i,j, sprintf('%4.2f',psummary(ccc(i),ccr(j))));
      set(h,'HorizontalAlignment','center','Color',clr);
      h2= text(i,j-0.35, sprintf('(%1d)',csummary(ccc(i),ccr(j))));
      set(h2,'HorizontalAlignment','center','Color',clr2,'Fontsize',get(h2,'Fontsize')*0.7);
    end
	end
%   set(gca,'XTick',1:length(ccr));
%   set(gca,'XTickLabel',names(ccr));
%   set(gca,'YTick',1:length(ccc));
%   set(gca,'YTickLabel',names(ccc));
  set(gca,'XTick',1:length(ccc));
  set(gca,'XTickLabel',names(ccc));
  set(gca,'YTick',1:length(ccr));
  set(gca,'YTickLabel',names(ccr));
end

xlabel('Actual Class');
ylabel('Predicted Class');
title('Confusion Matrix');
axis('square');
