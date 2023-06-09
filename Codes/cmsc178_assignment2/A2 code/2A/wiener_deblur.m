function I_deblur = wiener_deblur(I,B,k)
  % All input and output are of type double
  % Inputs:
  % I - input image 
  % B - blur kernel 
  % k - regularizzation parameter 
  %
  % Output:
  % I_deblur - deblurred image
 
if ( isa(I,'uint8') || isa(B,'uint8') )
  error('deblur: Image and blur data should be of type double.');
end

I = edgetaper(I,B);
Fi = fft2(I);
% modify the code below ------------------------------------------------

% 1. zero pad B and compute its FFT
pad_size    = floor((size(I) - size(B)) / 2);             % calculate pad size
padded_b    = padarray(B, pad_size, 0, 'both');           % zero pad B
F_b         =  fft2(padded_b, size(I, 1), size(I, 2));    % fourier representation of image B


% 2. compute and apply the inverse filter
F_inv       = zeros(size(I));                             % weiner function array
abs_F_b     = abs(F_b).^2;                                 
F_inv       = (Fi ./ F_b) .* (abs_F_b ./ (abs_F_b + k));  % weiner inverse filter


% 3. convert back to a real image
I_deblur    = real(ifft2(F_inv));


% 4. handle any spatial delay caused by zero padding of B
I_deblur    = ifftshift(I_deblur);

%
% you may need to deal with values near zero in the FFT of B etc
% to avoid division by zero's etc.

% modify the code above ------------------------------------------------


% NOTES:
%
% On the first step, zero padding is necessary but not required for wiener deconvolution.
% Applying zero padding ensures that the input image and kernel blur are of the same size
% for easier element-wise multiplication in the frequency domain.
%
% What happened here is that kernel blur is padded with zeros so that it will match the size of
% the image input. 

return

