% HU - Hu invariant moments calculator
%
% Usage: J = HU(<image>,<mormalise flag>
%
% Here <image> is either an Nx3 array of x,y and intensity values or
% and NxM greyscale image. The notmalise flag is set to true (or 1)
% will attempt to normalise the Hu monents post calculation.
%
% J is a 7x1 vector containing the calculated moments.
%
% Author: D.Gibbins (adelaide uni).
%
% PLEASE NOTE YOU PROBABLY WONT NEED THIS TO COMPLETE ASSIGNMENT 4 BUT FEEL
% FREE TO EXPERIMENT WITH THE HU MOMENTS IF YOU LIKE. THE NORMALISE FLAG MAY
% OR MAY NOT HELP YOU TO RESCALE THE RAW OUTPUT VALUES SO USE IT WITH CAUTION.
% - DG
%

function J = hu(xyi,normalise_flag)

if (nargin<2)
  normalise_flag=false;
end

if (size(xyi,2) > 3)
  % convert from an image (if req'd)
  I=xyi;
  [x,y]=meshgrid(1:size(I,1),1:size(I,2));
  ix = find(I>0);
  xyi = [ x(ix) y(ix) I(ix) ];
else
  if (min(xyi,3) < 0)
    disp('warning: negative intensity value in 2D moment estimation.');
  end
end

% centralise position
cx = mu(xyi,1,0)/mu(xyi,0,0);
cy = mu(xyi,0,1)/mu(xyi,0,0);
xyi(:,1)=xyi(:,1)-cx;
xyi(:,2)=xyi(:,2)-cy;

% normalised central moments
mu_11 = mu_sinv(xyi,1,1);
mu_20 = mu_sinv(xyi,2,0);
mu_02 = mu_sinv(xyi,0,2);
mu_21 = mu_sinv(xyi,2,1);
mu_12 = mu_sinv(xyi,1,2);
mu_30 = mu_sinv(xyi,3,0);
mu_03 = mu_sinv(xyi,0,3);

J(1) = mu_20 + mu_02;
J(2) = (mu_20-mu_02)^2 + (2*mu_11)^2;
J(3) = (mu_30-3*mu_12)^2 + (3*mu_21-mu_03)^2;
J(4) = (mu_30+mu_12)^2 + (mu_21+mu_03)^2;

J(5) = (mu_03-3*mu_12)*(mu_30+mu_12)*( (mu_30+mu_12)^2 - 3*(mu_21+mu_03)^2 ) + ...
  (3*mu_21-mu_03)*(mu_21+mu_03)*( 3*(mu_30+mu_12)^2 - (mu_21+mu_03)^2 ) ;

J(6) = (mu_20-mu_02)*( (mu_30+mu_12)^2 - (mu_21+mu_03)^2 ) + ...
  4*mu_11*(mu_30+mu_12)*(mu_21+mu_03);

J(7) = (3*mu_21-mu_03)*(mu_30+mu_12)*( (mu_30+mu_12)^2 - 3*(mu_21+mu_03)^2 ) - ...
  (mu_30-3*mu_12)^2*(mu_21+mu_03)*( 3*(mu_30+mu_12)^2 - (mu_21+mu_03)^2 );

% this is an 8th sometimes seen in gait estimation papers
J(8) = (mu_20 * mu_02) - mu_11^2;

if (normalise_flag)
  % normalise the Hu moments (these normalisations are based on various comments
  % found in papers and on the web).
  %
  % COMMENT - I AM NOT CONVINCED THAT THESE NORMALISATIONS ARE ALL THAT
  % USEFUL -DG.
  %
  J(1) = log( 10*(J(1)^2) );
  J(2) = log( (J(2)+0.0001)/0.0101) + 3;
  J(3) = log( (J(3)+0.0005)/0.0250) + 3;
  J(4) = log( (J(4)+0.0000001)/0.0000101);
  J(5) = sign(J(5))*(abs(J(5))^(1/3)); % - 3;
  J(6) = sign(J(6))*(abs(J(6))^(1/3));
  J(7) = sign(J(7))*(abs(J(7))^(1/3));

end


return

% ------------------------------------------------------------------------

function est = mu_sinv(xyi,p,q)
est = mu(xyi,p,q) / ( mu(xyi,0,0) ^((p+q+2)/2) );
return

function est = mu(xyi,p,q)
est = sum( (xyi(:,1).^p) .* (xyi(:,2).^q) .* (xyi(:,3)) );
return

% -------------------------------------------------------------------------
