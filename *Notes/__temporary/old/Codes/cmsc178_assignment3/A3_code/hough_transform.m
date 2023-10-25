function H = hough_transform(E,rhos,thetas)

% E - edge image
% rhos - range of rho values for transform array (eg. -50:0.5:50)
% thetas - range of thetas for array (eg. -90:1:90)
%
% H - resulting Hough array

E=double(E);


% find entry where rho=0, needed for array offset
%
p=polyfit(rhos,1:length(rhos),1);
zeroth_bin=round(polyval(p,0));
deltarho=(rhos(length(rhos))-rhos(1))/length(rhos);


% for each edge point add to accumulator array
%
[rows cols]=size(E);
H=zeros(length(rhos), length(thetas));
%scan each pixel in binary edge image.  If pixel = true, perform hough
%transform, otherwise jump to next pixel
for c=1:cols
  for r= 1:rows
    if E(r,c) ~= 0
      pk_bin_last = NaN;
      for k=1:length(thetas)
        %for the pixel, calculate a corhosponding rho for each
        % theta.
        pk=c*cos(thetas(k)*pi/180)+r*sin(thetas(k)*pi/180);
        pk_bin=round(pk/deltarho) + zeroth_bin;
        pk_bin = max(min(pk_bin,size(H,1)),1);
        %The larger the delta_rho and the smaller the rhos range the
        %courser the bin allocation, Therefore less likely to get
        %some lines, but if bin allocation has very fine
        %resolution, then may miss rough-multi pixel thick lines.
        
        if ( k==1)
          H(pk_bin,k)= H(pk_bin, k)+1;
        else
          if ( abs(pk_bin-pk_bin_last) ==1 )
            H(pk_bin,k)= H(pk_bin, k)+1;
          else
            if (pk_bin>pk_bin_last)
              H((pk_bin_last+0):pk_bin,k) = H((pk_bin_last+0):pk_bin,k) + 1;
            else
              H((pk_bin_last-0):-1:pk_bin,k) = H((pk_bin_last-0):-1:pk_bin,k) + 1;
            end
          end
        end
        pk_bin_last = pk_bin;
      end
    end
  end
end

figure;
imagesc(thetas,rhos,H);  %axis equal tight;
colormap(gray);
title('Hough Transform Estimate');
xlabel('Theta');
ylabel('Rho');
drawnow;

return
