% CHART_CORRECTION - calculate RGB mappings to correct for color imbalance 
%                    between values measured from reference and test charts 
% Usage:
%         RGB_map = chart_correction(RGB_reference,RGB_measured)
%
% RGB_reference - Mx3 list of reference RGB samples 
% RGB_measured  - Mx3 list of actual RGB samples 
%
% RGB_map - 256x3 lookup table of R,G and B colour corrections
%

function RGB_map = chart_correction(RGB_reference,RGB_measured)

% Here we need to use the difference between the measured RGB values
% and the reference RGB values to create a lookup tables for RGB which will
% map the measured values back into the reference.

% Here the result is result is to be returned as a 256x3 table which contains the
% correction for the red,green and blue values


% ---- INSERT YOUR CODE BELOW -----

% REPLACE THIS LINE WITH YOUR OWN CODE
RGB_map = round(255*rand(256,3)); % <--- for now this returns a dummy result

% HINT  - you can try and work these out from first principles or use interp1 or 
% polyfit/polyval to estimate the corrections from the measured to reference
% measurements for each of the values 0..255. Any fitted values outside 0..255 
% should be adjusted accordingly. Map values should be integers too.


% Fitting for Red Channel
p_Red = polyfit(RGB_reference(:,1), RGB_measured(:,1),2);
R_map = polyval(p_Red, 0:1:255);


% Fitting for Green Channel
p_Green = polyfit(RGB_reference(:,2), RGB_measured(:,2),2);
G_map = polyval(p_Green, 0:1:255);


% Fitting for Blue Channel
p_Blue = polyfit(RGB_reference(:,3), RGB_measured(:,3),2);
B_map = polyval(p_Blue, 0:1:255);


% Something





% ---- INSERT YOUR CODE ABOVE -----


return
