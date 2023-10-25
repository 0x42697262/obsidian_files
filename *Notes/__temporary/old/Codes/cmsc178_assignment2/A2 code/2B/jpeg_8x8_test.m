%
% simple test code for djpeg_8x8 solutions
%

Q=80;

% rand region
X = uint8(round(255*rand(8,8)));
% encode
[dc,ac] = jpeg_8x8(X,Q);
% decode
Y = djpeg_8x8(dc,ac,Q);
% rms error
rms=sqrt(sum(sum( (double(X)-double(Y)).^2 ))/numel(Y));

figure
colormap(gray(256));
subplot(2,2,1); image(X); title('Input');
subplot(2,2,2); image(Y); title('Decompressed');
subplot(2,2,3); imagesc(double(X)-double(Y)); 
title(sprintf('Difference (rms %4.2f)',rms)); 
colorbar;

% rand region
X = [ 255 255 0 0 0 0 0 0 ; 255 255 0 0 0 0 0 0 ; 0 0 255 255 0 0 0 0 ; ...
  0 0 255 255 0 0 0 0 ; 0 0 0 0 255 255 0 0 ;0 0 0 0 255 255 0 0 ; ...
  0 0 0 0 0 0 255 255 ; 0 0 0 0 0 0 255 255  ];
% encode
[dc,ac] = jpeg_8x8(X,Q);
% decode
Y = djpeg_8x8(dc,ac,Q);
% rms error
rms=sqrt(sum(sum( (double(X)-double(Y)).^2 ))/numel(Y));

figure
colormap(gray(256));
subplot(2,2,1); image(X); title('Input');
subplot(2,2,2); image(Y); title('Decompressed');
subplot(2,2,3); imagesc(double(X)-double(Y)); 
title(sprintf('Difference (rms %4.2f)',rms));
colorbar;



