%
% Compute the quantised coefficients for a given 8x8 jpeg region
%
% tile - 8x8 greyscale region (0..255)
% Q - quality factor 1..100 (eg. 80).
%
% dc_coeff  - quantised dc coefficient  of DCT
% ac_coeff - quantised ac coefficients (63) of DCT in zig-zag order
%
function [dc_coeff,ac_coeff] = jpeg_8x8(tile,Q)

% quantisation table used to quantise DCT coefs
Qtable = [ 16  11  10  16  24  40  51  61 ; ...
	    12  12  14  19  26  58  60  55 ; ...
	    14  13  16  24  40  57  69  56 ; ...
	    14  17  22  29  51  87  80  62 ; ...
	    18  22  37  56  68 109 103  77 ; ...
	    24  35  55  64  81 104 113  92 ; ...
	    49  64  78  87 103 121 120 101 ; ...
	    72  92  95  98 112 100 103  99 ];
    
% centre image data about greylevel 128
tile=double(tile)-128;

% Q scale factor used in quantisation step
if (Q<=50)
  qt_scale = 50/Q;
else
  qt_scale = 2-Q/50;
end
% get raw DCT coeffs of tile
Y = dct(tile);
% quantise coefficients
Yq = round(Y./(Qtable*qt_scale));
% get DC coefficient (top left entry in DCT)
dc_coeff = Yq(1,1);

% zig zag along rows
ll = 1; mm = 2; ac_count = 1; direction = 1;
ac_coeff=zeros(1,63);
for kk = 3:16
  if (direction)
    for ll = max(1,kk-8):min(kk-1,8)
      ac_coeff(ac_count) = Yq(min(8,ll),kk-min(8,ll));
      ac_count = ac_count+1;
    end
  else
    for ll = max(1,kk-8):min(kk-1,8)
      ac_coeff(ac_count) = Yq(kk-min(8,ll),min(8,ll));
      ac_count = ac_count+1;
    end
  end
  direction = 1-direction;
end

% ----------------------------------------------------------------------










