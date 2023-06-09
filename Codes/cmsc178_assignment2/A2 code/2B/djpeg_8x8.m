%
% Compute the quantised coefficients for a given 8x8 jpeg region
%
% tile - 8x8 greyscale region (0..255)
% Q - quality factor 1..100 (eg. 80).
%
% dc_coeff  - quantised dc coefficient  of DCT
% ac_coeff - quantised ac coefficients (63) of DCT in zig-zag order
%
function tile = djpeg_8x8(dc_coeff,ac_coeff,Q)

% quantisation table used to quantise DCT coefs
Qtable = [ 16  11  10  16  24  40  51  61 ; ...
	    12  12  14  19  26  58  60  55 ; ...
	    14  13  16  24  40  57  69  56 ; ...
	    14  17  22  29  51  87  80  62 ; ...
	    18  22  37  56  68 109 103  77 ; ...
	    24  35  55  64  81 104 113  92 ; ...
	    49  64  78  87 103 121 120 101 ; ...
	    72  92  95  98 112 100 103  99 ];
    
% init quantised 8x8 coef array
Zq=zeros(8,8);


%-----------change code from here --------------------------------
%

% 1. copy DC back in
Zq(1,1)   = dc_coeff;
 
% 2. order zig-zag access and copy AC back
ll = 1; mm = 2; ac_count = 1; direction = 1;
for kk = 3:16
  % using max(1, kk-8) restricts the range of the lower limit from 1 to 8
  % using min(kk-1, 8) restricts the range of the upper limit does not exceed 8
  % checking the direction if 1 or 0 (true or false) sets the direction to being regular or reverse
  % the quantized coefficient array Zq will be assigned with the current ac_coeff array based on the index ac_count
  % we need to update ac_count in order to use the next ac coefficient value to avoid reusing it
  if (direction)
    for ll = max(1,kk-8):min(kk-1,8)
      Zq(min(8,ll),kk-min(8,ll))  = ac_coeff(ac_count);
      ac_count                    = ac_count+1;
    end
  else
    for ll = max(1,kk-8):min(kk-1,8)
      Zq(kk-min(8,ll),min(8,ll))  = ac_coeff(ac_count);
      ac_count                    = ac_count+1;
    end
  end
  % This flips the direction (a boolean-like)
  direction = 1-direction;                                
end

% 3. Q scale factor used in quantisation step
if (Q<=50)
  qt_scale = 50/Q;
else
  qt_scale = 2-Q/50;
end

% 4. estimate original Z coefficients using Zq etc
Z = Zq.*(Qtable*qt_scale);

% 5. inverse dct (assign to variable 'tile')
tile = idct(Z);



%-----------change code above here --------------------------------

% centre image data about greylevel 128
tile=uint8(tile+128);

% ----------------------------------------------------------------------









