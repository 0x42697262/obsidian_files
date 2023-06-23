% CHULL_3X3 - simple convex hull
%
% I2 = CHULL_3X3(I,<n>)
%
% n = number of convex hull iterations, default Inf (ie. until complete)

function I2 = chull_3x3(I,n)

if (nargin<2)
  n=Inf;
end

T{1} = [0 1 1; 0 -1 1; -1 0 1];
T{2} = fliplr(T{1});
T{3} = flipud(T{1});
T{4} = fliplr(flipud(T{1}));
T{5} = T{1}';
T{6} = fliplr(T{5});
T{7} = flipud(T{5});
T{8} = flipud(fliplr(T{5}));

iterations=0;
changing=true;
while ( (iterations < n) && (changing) )
  iterations=iterations+1;
  I2 = I;
  for i=1:8
    I2 = I2 | hitormiss_3x3(I,T{i});
  end
  changing = ( sum(sum(abs(I-I2))) > 0 );
  I = I2;
end

return






