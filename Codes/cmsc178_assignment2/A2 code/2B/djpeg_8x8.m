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
% 2. order zig-zag access and copy AC back
% 3. Q scale factor used in quantisation step
% 4. estimate original Z coefficients using Zq etc
% 5. inverse dct (assign to variable 'tile')

tile = round(255*rand(8,8))-128; % GENERATE SOME RANDOM RESULTS (REMOVE THIS LINE)

%-----------change code above here --------------------------------

% centre image data about greylevel 128
tile=uint8(tile+128);

% ----------------------------------------------------------------------









