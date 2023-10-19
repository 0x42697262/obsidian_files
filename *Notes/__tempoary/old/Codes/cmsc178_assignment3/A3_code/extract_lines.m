function RT = extract_lines(H,rhos,thetas,N)

% H - hough transforms
% rhos - related rho values
% thetas - related theta values
% N - number of peaks to identify
%
% RT - a N rows by 2 columns array of the peak rho and theta values

RT = zeros(N,2);

% -------------------- put your code in below ---------------------------

% NOTES: the peaks appear as elongated reagions of large values in the
% hough data. Simply identifying local maxima may not be enough as the
% central peak is sometimes slightly reduced if the lines are not exactly
% straight. You will also need to make sure you do not pick multiple
% peaks which are associated with the same line estimate.

% The suggested method of approach is to look for a global maxima over a
% region LARGER than a simple 5x5 neighbourhood. This maxima is then
% treated as the strongest line and the rho,theta value recorded. The
% region around this point is then zeroed, and the process repeated for
% the next brightest line. ie.
%
% for i=1 to N
%    1. find brightest maxima using local neigbourhood estimates (this will 
%        probably require a double for loop etc)
%    2. record the rho,theta value
%    3. blank out the neighbourhood around the identified maxima

for k = 1:N
    % -- Find the brightest peak in the Hough transform
    [~, max_index] = max(H(:));
    [row, col] = ind2sub(size(H), max_index);
    
    % Record the rho, theta position of the peak
    RT(k, 1) = rhos(row);
    RT(k, 2) = thetas(col);
    
    % Supress the region around the peak in the Hough transform
    neighborhood_size = 10;  % Adjust the size of the neighborhood as needed
    rows_range = max(1, row-neighborhood_size):min(size(H, 1), row+neighborhood_size);
    cols_range = max(1, col-neighborhood_size):min(size(H, 2), col+neighborhood_size);

    % Zero out the neighborhood
    H(rows_range, cols_range) = 0;
end

% ---------------------put your code in above ---------------------------

figure;

imagesc(thetas,rhos,H); %axis equal tight;
colormap(gray);
title('Hough Transform - Detected Maximas');
xlabel('Theta');
ylabel('Rho');
hold on;
plot(RT(:,2),RT(:,1),'bo');
hold off;
drawnow;

return

% -----------
% END OF FILE
