%
% DETERMINE the best K to be able to read the number plates
%

B=fspecial('gaussian',65,10);

I = double(imread('example3.png'))/255; I=I(:,:,1);

k=input('Enter an estimate for k (1 .. 0.00001):');

Iinv = wiener_deblur(I,B,k);

figure;
colormap(gray);
subplot(1,5,[1 2]);
imagesc(I); axis equal tight; caxis([0 1]);
title('Blurry Number Plates');
subplot(1,5,3);
imagesc(B); axis equal tight;
title('PSF (Guess)');
subplot(1,5,[4 5]);
imagesc(Iinv); axis equal tight; caxis([0 1]);
title('Deconvoled Image');
drawnow;