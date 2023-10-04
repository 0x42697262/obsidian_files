% HAND_SIGNATURE - estimate the signature of the given hand region
%
% S = HAND_SIGNATURE(B)
%
% S is a 1x260 element array of distances one for each angle between 0 and
% 359 degrees.

function S = hand_signature(B)
%
% 1.	Find the centroid of the hand and the coordinates of pixels on the hand boundary (this can be readily obtained using regionprops)
% 2.	Subtract the centroid position (cx,cy) from the boundary pixel coordinates to give a list of points centred on (0,0).
% 3.	For each rotation X from 0 to 359 degrees:
%   a.	Rotate the coordinates by angle X
%   b.	Find the edge points within approximately 2 pixels of the y-axis.
%   c.	Set the signature for angle X to be the maximum y value of the identified points. If the value is less than zero then set it to zero.

% ----- INSERT YOUR CODE HERE ---


% 1.	Find the centroid of the hand and the coordinates of pixels on the hand boundary (this can be readily obtained using regionprops)
centroid = regionprops(B, {'Centroid'});
boundary = cell2mat(bwboundaries(B));

% 2.	Subtract the centroid position (cx,cy) from the boundary pixel coordinates to give a list of points centred on (0,0).
center_bound_y  = (boundary(:,1) - centroid.Centroid(2)) * -1;
center_bound_x  = boundary(:,2) - centroid.Centroid(1) ;

% 3.	For each rotation X from 0 to 359 degrees:
S = zeros(1,360);
for i = 0:359
    %   	Rotate the coordinates by angle X
    angle   = i * pi/180;
    x_prime = center_bound_x * cos(angle) + center_bound_y * sin(angle);
    y_prime = -center_bound_x * sin(angle) + center_bound_y * cos(angle);
    
    %   	Find the maximum edge points within approximately 2 pixels of the y-axis.
    current_maximum = 0;
    for j = 1:numel(y_prime)
        if x_prime(j) >= -1 && x_prime(j) <= 1 && y_prime(j) > current_maximum
            current_maximum = y_prime(j);
        end
    end
    %   	Set the signature for angle X to be the maximum y value of the 
    % identified points. If the value is less than zero then set it to zero.
    % No need to check if value is less than zero as the current_maximum was
    % already set to 0. If a negative value was to be found in the 2 pixels
    % near the y-axis, current_maximum wouldn't be set.
    S(i+1) = current_maximum;
end

% ----- INSERT YOUR CODE ABOVE ----

% % PLOT - use this for debugging as needed
%subplot(2,2,1);
%imagesc(B);
%title('Region');
%subplot(2,1,2);
%plot(S); title('Signature');
%xlabel('Angle (deg)');
%ylabel('Distance');
%drawnow;

return
