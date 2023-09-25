
I = imread('skel_image.tif');
I = double(I)/255;

subplot(2,2,1);
imagesc(I); colormap(gray);
title('Binary image');

CH1 = skel_3x3(I,1);
subplot(2,2,2);
imagesc( CH1 + I );
title('Skel 1-step + Original'); 
drawnow

CH5 = skel_3x3(I,5);
subplot(2,2,3);
imagesc( CH5 + I );
title('Skel 5-steps + Original');
drawnow

CHinf = skel_3x3(I,inf);
subplot(2,2,4);
imagesc( CHinf + I );
title('Skel inf-steps + Original');
drawnow
