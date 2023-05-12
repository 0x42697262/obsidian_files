function I_deblur = wiener_deblur(I,B,k)
 
if ( isa(I,'uint8') || isa(B,'uint8') )
  error('deblur: Image and blur data should be of type double.');
end

I = edgetaper(I,B);
Fi = fft2(I);
% modify the code below ------------------------------------------------

% this section is just dummy code - delete it

F_deblur = Fi;
I_deblur = real( ifft2(F_deblur) );

% Here you will need to:
% 1. zero pad B and compute its FFT
% 2. compute and apply the inverse filter
% 3. convert back to a real image
% 4. handle any spatial delay caused by zero padding of B
%
% you may need to deal with values near zero in the FFT of B etc
% to avoid division by zero's etc.

% modify the code above ------------------------------------------------

return

