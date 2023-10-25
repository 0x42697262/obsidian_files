function Imatch = hitormiss_3x3(I, M)
    if (ndims(I)==3)
      I=I(:,:,2);
    end
    if (isa(I,'uint8'))
      I=double(I)/255;
    end
    
% --------------- INSERT YOUR CODE BELOW -----------------
    % -- Compute the complement of the binary image
    An = ~I;
    
    % -- Perform erosion using the structure elements for "set" and "unset" pixels
    E1 = erode_3x3(I, M == 1);
    E2 = erode_3x3(An, M == -1);
    
    % -- Compute the intersection of the two erosions
    Imatch = E1 & E2;
% --------------- INSERT YOUR CODE ABOVE -----------------    

end

function E = erode_3x3(I, S)
% --------------- INSERT YOUR CODE ABOVE -----------------    
    % -- Get the size of the input image
    [rows, cols] = size(I);

    % -- Create an output matrix for the erosion result
    E = false(size(I));

    % -- Perform erosion using the structure element
    for i = 2:rows-1
        for j = 2:cols-1
            % -- Extract the neighborhood window
            window = I(i-1:i+1, j-1:j+1);

            % -- Check if the window matches the structure element
            if all(window(S))
                E(i, j) = true;
            end
        end
    end

% --------------- INSERT YOUR CODE ABOVE -----------------    
end
