
N=input('Enter number of lines to search for (eg. 10):');
if (isempty(N)); N=10; end

% TEST 1 - box image - log edges
I = imread('box.tif');
E = double(imread('box_log_edge.tif'))/255;
figure;subplot(1,2,1);imagesc(I); axis equal tight; subplot(1,2,2);imagesc(E);axis equal tight; colormap(gray);
diag=round(sqrt(sum(size(E).^2)));
H  = hough_transform(E,[-diag:diag],[-90:0.5:90]);
rt = extract_lines(H,[-diag:diag],[-90:0.5:90],N);
display_lines(I,rt);

% For reference: this is the approximate solution
%display_lines(I,[0 -30; 34 -31; 45 59 ; 78 60]);

disp('Press return...');
pause;

% TEST 2 - lift edge image (this one is again quite difficult so expect a few 'bad' line estimates))
I = imread('lift_crop.tif');
E = double(imread('lift_crop_log_edge.tif'))/255;
figure;subplot(1,2,1);imagesc(I);axis equal tight; subplot(1,2,2);imagesc(E);axis equal tight; colormap(gray);
diag=round(sqrt(sum(size(E).^2)));
H  = hough_transform(E,[-diag:diag],[-90:0.5:90]);
rt = extract_lines(H,[-diag:diag],[-90:0.5:90],N);
display_lines(I,rt);

% add your own testing code as required below



