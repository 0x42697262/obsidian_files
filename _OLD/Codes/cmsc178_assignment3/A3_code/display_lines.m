function llist = display_lines(I,rt)

% I - input image
% rt - rho,theta pairs describing line segments

figure;
imagesc(I);
axis equal tight;
ax=axis;
if (size(I,3)==1)
  colormap(gray);
end
title('Line Estimates');

llist=NaN*ones(size(rt,1),4);
for n=1:size(rt,1)
  rho=rt(n,1);
  theta=rt(n,2) * (pi/180);
  % calsulate point on the line segment
  if ( abs( cos(theta) ) > 0.5 )
    x1=1;
    x2=size(I,2);
    y1= (rho - x1*cos(theta))/sin(theta);
    y2= (rho - x2*cos(theta))/sin(theta);
  else
    y1=1;
    y2=size(I,1);
    x1=(rho - y1*sin(theta))/cos(theta);
    x2=(rho - y2*sin(theta))/cos(theta);
  end
  hold on; plot([x1 x2],[y1 y2],'-'); hold off;
  llist(n,:)=[x1 y1 x2 y2];
end

% try and force display to clip lines (possible fix for 2015b or later)
axis(ax);
drawnow;

return

%------------
% END OF FILE