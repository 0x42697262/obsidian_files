
% PART 1 - simple BOX image tests

I = double(imread('components.tif'))/255;

% 13x13 filter
[E,B,G] = log_edge(I,13);
figure
subplot(2,2,1);
imagesc(I); title('Image'); axis equal tight; 
subplot(2,2,2);
imagesc(G); title('LoG Output'); axis equal tight; 
subplot(2,2,3);
imagesc(B); axis equal tight; title('LoG Filter');
subplot(2,2,4);
imagesc(E); title('Edges'); axis equal tight; 
colormap(gray);
drawnow;

% 9x9 filter
[E,B,G] = log_edge(I,15);
figure
subplot(2,2,1);
imagesc(I); title('Image'); axis equal tight; 
subplot(2,2,2);
imagesc(G); title('LoG Output'); axis equal tight; 
subplot(2,2,3);
imagesc(B); axis equal tight; title('LoG Filter');
subplot(2,2,4);
imagesc(E); title('Edges'); axis equal tight; 
colormap(gray);
drawnow;



% 35x35 filter -- my own test
[E,B,G] = log_edge(I,35);
figure
subplot(2,2,1);
imagesc(I); title('Image'); axis equal tight; 
subplot(2,2,2);
imagesc(G); title('LoG Output'); axis equal tight; 
subplot(2,2,3);
imagesc(B); axis equal tight; title('LoG Filter');
subplot(2,2,4);
imagesc(E); title('Edges'); axis equal tight; 
colormap(gray);
drawnow;

% 5x5 filter -- my own test
[E,B,G] = log_edge(I,5);
figure
subplot(2,2,1);
imagesc(I); title('Image'); axis equal tight; 
subplot(2,2,2);
imagesc(G); title('LoG Output'); axis equal tight; 
subplot(2,2,3);
imagesc(B); axis equal tight; title('LoG Filter');
subplot(2,2,4);
imagesc(E); title('Edges'); axis equal tight; 
colormap(gray);
drawnow;
%
% % ---------------------------------------------
%
% % part 2 - other example images
%
I = double(imread('bolts.tif'))/255;
[E,B,G] = log_edge(I,11);
figure
subplot(2,2,1);
imagesc(I); title('Image'); axis equal tight; 
subplot(2,2,2);
imagesc(G); title('LoG Output'); axis equal tight; 
subplot(2,2,3);
imagesc(B); axis equal tight; title('LoG Filter');
subplot(2,2,4);
imagesc(E); title('Edges'); axis equal tight; 
colormap(gray);
drawnow;
%
I = double(imread('engine.tif'))/255;
[E,B,G] = log_edge(I,13);
figure
subplot(2,2,1);
imagesc(I); title('Image'); axis equal tight; 
subplot(2,2,2);
imagesc(G); title('LoG Output'); axis equal tight; 
subplot(2,2,3);
imagesc(B); axis equal tight; title('LoG Filter');
subplot(2,2,4);
imagesc(E); title('Edges'); axis equal tight; 
colormap(gray);
drawnow;

