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

## 3 Results & Discussion
## 4 Comments & Conclusion

---



# Exercise 1B – ( 2% ) – Image Contrast Enhancement

## 1 Background of the Problem


## 2 Procedure


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
