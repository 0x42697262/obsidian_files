function Inoisy = noisy_image(I,nsigma)
 
% naively add white noise to an image (assuming image data in range 0..1)
% nsigma is the noise standard deviation

Inoisy = I + nsigma*randn(size(I));

return

