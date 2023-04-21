# Exercise 1A – ( 3% ) – Colour Balancing using a Reference Chart
## 1 Background of the Problem


## 2 Procedure
### Step 1
First, I set the number of rows and columns which is based on the color chart.
```matlab
number_of_rows      = 4;
number_of_columns   = 6;
```

Next is to set the output RGB list to zeros which is based on the total patches in the color chart.
```matlab
RGB_list  = zeros(number_of_rows * number_of_columns, 3);
```

Since we know that the color chart has a black background and are separated with gaps, we have to get its offset along with its gap size. We also must consider the size of the patch. 
Assuming that the patch color is consistent all over, we can simply just get the first pixel value or the center value of the patch. However, if it's not consistent, we can get the average of the patch color.

Coding what I mentioned above seems annoying, so what I instead do is grab the center pixel since we know that the patch has consistent colors (except the edges) and hardcode it.
```matlab
OFFSET_LEFT   = 55;
OFFSET_TOP    = 64;
PATCH_WIDTH   = 238;
PATCH_HEIGHT  = 232;
PATCH_GAP     = 14;
PATCH_MID_V   = PATCH_HEIGHT/2;
PATCH_MID_H   = PATCH_WIDTH/2;
```

Next thing to do is to loop through the rows and colums of the color chart. We have to get the values of each patches and put it to the RGB list.
The general formula for this is to get the index of the color then its RGB fields: `RGB_list(patch_index, RGB) = chart_image(height, width, rgb);`
```matlab
for row = 1:number_of_rows
  for column = 1:number_of_columns
    patch_index   = (row - 1) * number_of_columns + column;
    height        = OFFSET_TOP + PATCH_MID_V + (row - 1) * (PATCH_HEIGHT + PATCH_GAP); 
    width         = OFFSET_LEFT + PATCH_MID_H + (column - 1) * (PATCH_WIDTH + PATCH_GAP);
    
    RGB_list(patch_index, :)  = chart_image(height, width, :);
  end
end
```


### Step 2
First create a list of RGB maps all initiated to zeros.
```matlab
RGB_map         = zeros(256, 3);
```

Since the code for fitting the RGB values are already provided, next thing to do is to store their unsigned integer value to the `RGB_map` to ensure that the values are 8 bits or within 0 to 255 range.
```matlab
RGB_map(:, 1)   = uint8(R_map);
RGB_map(:, 2)   = uint8(G_map);
RGB_map(:, 3)   = uint8(B_map);
```

### Step 3
Initalize a list of zeros to store the corrected image values.
```matlab
adjusted_image  = zeros(size(RGB_image));
```

Then, the code iterates over each pixel in the input image using nested for-loops. For each pixel, the code looks up the corresponding R, G, and B values in the RGB lookup table, which is done by indexing the lookup table using the RGB values of the current pixel. The corrected R, G, and B values are then stored in the corresponding positions of the adjusted_image list.
```matlab
for row = 1:size(RGB_image, 1)
  for column = 1:size(RGB_image, 2)
    adjusted_image(row, column, 1) = RGB_map(RGB_image(row, column, 1) + 1, 1);
    adjusted_image(row, column, 2) = RGB_map(RGB_image(row, column, 2) + 1, 2);
    adjusted_image(row, column, 3) = RGB_map(RGB_image(row, column, 3) + 1, 3);
  end
end
```

## 3 Results & Discussion
## 4 Comments & Conclusion

---



# Exercise 1B – ( 2% ) – Image Contrast Enhancement

## 1 Background of the Problem


## 2 Procedure
### Step 1
This step is simply the implementation of the function of the histogram equalization. To make life easier, using `hist()` function makes it easier although MATLAB says to use `histogram()`.
```matlab
histogram_result  = histcounts(img(:), 0:255);
```

After acquiring the values of the histogram, compute the cumulative distribution function.
```matlab
cdf               = cumsum(hist_result);
```

And proceed to calculate histogram map:
```matlab
equalization_map  = uint8((cdf / max(cdf)) * 255);
```

Replace the original pixel values with the equalized values using the lookup table and return the replaced image as a double image.
```matlab
new_img           = equalization_map(img + 1);
eq_img            = double(new_img) / 255;
```


## 3 Results & Discussion


## 4 Comments & Conclusion


# Exercise 1C – ( 2% ) – A Simple median Filter
## 1 Background of the Problem


## 2 Procedure


## 3 Results & Discussion


## 4 Comments & Conclusion


# Exercise 1D – ( 3% ) – A "Smart" Edge Preserving Noise Filter
## 1 Background of the Problem


## 2 Procedure


## 3 Results & Discussion


## 4 Comments & Conclusion


# Exercise 1E– (2%) – Written Questions



---
Github Reposity: [CMSC178 Assignment 1](https://github.com/KrulYuno/obsidian_files/tree/master/Codes)