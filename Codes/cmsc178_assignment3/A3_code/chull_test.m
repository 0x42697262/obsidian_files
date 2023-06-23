
I = imread('chull_image.tif');
I = double(I)/255;

subplot(2,2,1);
imagesc(I); colormap(gray);
title('Binary image');

CH1 = chull_3x3(I,1);
subplot(2,2,2);
imagesc( CH1 + I );
title('CHull 1-step + Original'); 
drawnow

CH5 = chull_3x3(I,5);
subplot(2,2,3);
imagesc( CH5 + I );
title('CHull 5-steps + Original');
drawnow

CHinf = chull_3x3(I,inf);
subplot(2,2,4);
imagesc( CHinf + I );
title('CHull inf-steps + Original');
drawnow
