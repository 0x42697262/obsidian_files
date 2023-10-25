
I = imread('hitmiss_image.tif');
I = double(I(:,:,1))/255;


T1 = [ -1 1 -1 ; 1 1 1 ; -1 1 -1 ]; % simple cross template
B1 = hitormiss_3x3(I,T1);


T2 = [ -1 0 -1 ; 0 1 0 ; -1 0 -1 ]; % centre set & zero diagonals
B2 = hitormiss_3x3(I,T2);

subplot(2,3,1); imagesc(I); colormap(gray); title('Input Image');

subplot(2,3,2); imagesc(T1); title('Template 1'); caxis([-1 1]);
subplot(2,3,3); imagesc(B1); title('Match 1');

subplot(2,3,5); imagesc(T2); title('Template 2'); caxis([-1 1]);
subplot(2,3,6); imagesc(B2); title('Match 2');

drawnow;

