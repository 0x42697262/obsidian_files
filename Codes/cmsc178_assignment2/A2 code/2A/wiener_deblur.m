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
pad_size            = floor((size(I) - size(B)) / 2);             % calculate pad size
padded_b            = padarray(B, pad_size, 0, 'both');           % zero pad B
F_blur_kernel_fft   =  fft2(padded_b, size(I, 1), size(I, 2));    % fourier representation of image B


% 2. compute and apply the inverse filter
wiener_inverse_filter   = zeros(size(I));                         % weiner function array
abs_F_blur_kernel_fft   = abs(F_blur_kernel_fft).^2;                                 
wiener_inverse_filter   = (Fi ./ F_blur_kernel_fft) .* (abs_F_blur_kernel_fft ./ (abs_F_blur_kernel_fft + k));  % weiner inverse filter


% 3. convert back to a real image
I_deblur    = real(ifft2(wiener_inverse_filter));


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
%
%
% On the second step, notice that inversing the filter requires division which sometimes can lead
% to instabilities and artifacts in the frequency domain if the divisor contains small or zero values.
% By taking the absolute value of blur kernel FFT or blur spectrum and then squaring it, this avoids
% dividing by zero.
% Wiener deconvolution algorithm requires us to calculate the magnitude squared of the Fourier representation
% of the blur kernel. Not taking the absolute values of the magnitude would lead to possibilities of using
% zero, negative, and complex numbers which we do not want that when using Wiener inverse filter. 
% The purpose of taking the absolute value ensures that we only want the magnitude information.
%
%
% On the third step, we converted the image from spatial domain to frequency domain and extracted the real values
% of the complex number that ifft2() function produced. This effectively reconstructs the image.

return

