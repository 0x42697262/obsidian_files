% SKEL_3X3 - simple skeletonisation
%
% I2 = THIN_3X3(I,<n>)
%
% n = number of iterations, default Inf (ie. until complete)

function I2 = skel_3x3(I,n)

if (nargin<2)
  n=Inf;
end

Ta = [ -1 -1 -1 ; 0 1 0 ; 1 1 1];
Tb = [ 0 -1 -1 ; 1 1 -1 ; 0 1 0 ];
T{1} = Ta;
T{2} = Ta';
T{3} = flipud(Ta);
T{4} = flipud(Ta)';

T{5} = Tb;
T{6} = Tb';
T{7} = flipud(Tb);
T{8} = fliplr(Tb)';

T = T([1 5 2 6 3 7 4 8]);

iterations=0;
changing=true;
while ( (iterations < n) && (changing) )
  iterations=iterations+1;
  
  I2 = I;
  for i=1:8
     Idel = hitormiss_3x3(I2,T{i});
     I2 = I2 & (Idel < 1);
  end

  changing = ( sum(sum(abs(I-I2))) > 0 );
  I = I2;

end

return






