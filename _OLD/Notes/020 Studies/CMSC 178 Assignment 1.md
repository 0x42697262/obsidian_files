	# Exercise 1A – ( 3% ) – Colour Balancing using a Reference Chart
## 1 Background of the Problem
The objective of this exercise is to implement three functions that extract RGB color samples from a color chart patch, map the RGB values to correct color imbalances between the reference and test charts, and apply the correction to an image. This exercise presents an opportunity to learn and develop color balancing skills by using a reference chart. 

The three files used in this exercise are:
1. `get_chart_values.m` : This function takes a color sample from a color chart and adds it to a list of RGB color patches.
2. `chart_correction.m` : This function calculates the RGB mappings needed to adjust for color imbalances between the values measured from reference and test charts.
3. `apply_rgb_map.m` : This function replaces the red (R), green (G), and blue (B) color values in an image with new values based on a supplied lookup table.

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
 I have tested the following three functions using three input images with varying parameters. The input images consist of a reference image and a corresponding image with poor RGB values. During processing, the image is first passed through the function that extracts reference image values, followed by the function that maps the RGB values, and finally the function that corrects the input image. The output of this process is a fixed image that accurately represents the original subject's color.

This is the resulting output of the corrected image.
![[Pasted image 20230424002010.png]]

Another example of the same picture but with different bad chart values.
![[Pasted image 20230424010811.png]]

Third example input image.
![[Pasted image 20230424011009.png]]

The output will always be the same for every identitical image since the input parameter is simply putting an image to the function and taking their RGB values into a list. If an input image where to have been modified to have a bad image result in another parameter, then the image would still be fixed. 

In addition to using regular images as inputs, I also experimented with using a completely white image as the input. The resulting output is displayed below.
![[Pasted image 20230425195524.png]]

I previously noted that the function does not have any configurations or parameters to adjust, but we can change the input image's tone levels. The previous input images had a bad image tone level of `50%`. Decreasing this value would provide exact results. However, when I increased the tone level percentage to `1000%`, the resulting image would mess up the output image.
![[Pasted image 20230425195907.png]]

The bad image is somehow identical to the reference image, meaning that when you fix a "good image" in this case, the opposite would effect would happen. It would turn a good image into a bad image. As for the example image below, the bad image is not the same as the reference image however the fixed image still resulted into a bad image.

![[Pasted image 20230425200219.png]]


## 4 Comments & Conclusion
In this exercise, the function only takes an input image as a parameter so there is nothing to be configured to have the most optimal output. 

For improving the output image, here's a few suggestions to take:
1. Use vectorization: The current code uses nested loops to iterate over every pixel in the image. However, this approach can be slow and inefficient, especially for large images. A more efficient approach would be to use vectorization to perform the operation on the entire image at once. This can be done using MATLAB's array indexing and broadcasting capabilities.
2. Use preallocation: The code currently initializes the adjusted_image matrix to zeros at every iteration of the loop. This can be slow, especially for large images. A more efficient approach would be to preallocate the matrix outside the loop, and then fill in the values inside the loop.
3. Check the size of the RGB_map: The code assumes that the RGB_map is a 256x3 matrix. However, if the size of the map is different, the code will not work correctly. It is important to check the size of the RGB_map before applying it to the image.

There are several limitations of this code:
1. **Limited lookup table size**: The code assumes that the lookup table is 256x3, which limits the number of colors that can be used to map the RGB values. If a higher color depth is required, the lookup table size will need to be increased, which can be computationally expensive.
2. **Limited color accuracy**: The code maps the RGB values independently, which can result in inaccurate color representation. The RGB triples do not represent actual colors in the image, and this is not a true colormap. This means that some color information may be lost during the mapping process.
3. **No support for non-RGB images**: The code only works with RGB images and cannot be used with other color spaces, such as grayscale or indexed color images. If the input image is not in the correct format, the code will not work correctly.
4. **No error handling for out-of-range values**: The code assumes that the input image and lookup table have values within the range of 0 to 255. If there are any values outside of this range, the code will not work correctly. It is important to handle these out-of-range values appropriately to avoid errors or incorrect output.
5. **Slow performance for large images**: The code uses nested loops to iterate over every pixel in the image, which can be slow and inefficient for large images. Using vectorization can improve the performance, but this may not be enough for extremely large images

---



# Exercise 1B – ( 2% ) – Image Contrast Enhancement

## 1 Background of the Problem
The objective of this exercise is to implement a function that improves the contrast of an image using histogram equalization without relying on built-in MATLAB Image Processing Toolbox functions. Histogram equalization is a technique used to adjust the contrast of an image by redistributing the pixel values to cover a wider range of intensities. This exercise provides an opportunity to develop a deeper understanding of image processing techniques and to gain experience in implementing them using MATLAB.

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
In this exercise, the function histogram equalization was tested on three different input images. The results of the testing showed that the function worked well as expected. The function only requires the input image itself as a parameter and does not need any other configuration to produce different image outputs.

To evaluate the performance of the function, two gray colored images and one full colored image were used as input. The choice of a colored image was made to verify if the code worked correctly for such images. However, it should be noted that if an input image is in the RGB color space instead of grayscale, the histogram equalization function may not be applicable, and it would instead require a separate exercise to solve this problem which was already completed on Exercise 1A. Nevertheless, the code function worked as expected similar to Exercise 1A Color Correction / Balancing for the RGB input image.

Sample inputs:
![[Pasted image 20230425180414.png]]
![[Pasted image 20230425180439.png]]
![[Pasted image 20230425180500.png]]
![[Pasted image 20230425180508.png]]
![[Pasted image 20230425180640.png]]
![[Pasted image 20230425180645.png]]

## 4 Comments & Conclusion
Given that the exercise involves a single function which exclusively takes an input image as a parameter, no further configurations are required to optimize the output image. 

Below are several approaches that could be taken to enhance the function's ability to produce high-quality image outputs:
1. Incorporate adaptive histogram equalization (AHE) or contrast-limited adaptive histogram equalization (CLAHE).
	1. AHE and CLAHE divide the image into small regions and apply histogram equalization to each region separately to enhance contrast, leading to better results, particularly for images with uneven illumination or varying contrast levels.
 2. Use a different method to compute the equalization map, such as the cumulative distribution function (CDF) of the image pixels' intensity values or incorporate techniques like gamma correction to enhance the overall visual quality of the image.
 3. Incorporate error handling and input validation to ensure the function can handle a wide range of input images without crashing or producing incorrect results.
	 1. Add appropriate checks to handle input images with unusual sizes or pixel formats.

Below are several limitations of the function code:
1. The function assumes that the input image is in the range 0 to 1, and therefore may not work properly for images with a different range of pixel values.
2. The function only performs histogram equalization and does not include other image enhancement techniques such as noise reduction or sharpening.
3. The function uses a fixed equalization map for all images and does not adapt to the characteristics of the input image, which may result in suboptimal results for certain images.
4. The function only works with 2D grayscale images and does not support color images or 3D images.
5. The function does not include error handling or input validation, which may cause errors or produce incorrect results for certain input images.

# Exercise 1C – ( 2% ) – A Simple median Filter
## 1 Background of the Problem
The objective of this exercise is to implement a simple median filter with the dimensions of MxN pixels by modifying the provided code template, without using library functions from MATLAB Image Processing Toolbox. The exercise includes a pre-existing function, `median_filter.m`, and a testing function, `median_test.m`, which evaluates the efficacy of our solution by removing salt and pepper noise from the input image.


## 2 Procedure
### Step 1
Pad the image dimension arrays in the edges. There are two ways to pad the edge arrays, either using zero padding or pixel replication. For this code, using pixel replication is better and MATLAB `padarray()` function already exists.
```matlab
padded_img  = padarray(img, [floor(M/2) floor(N/2)], 'symmetric');
```

Next is to make a new image to store the results based on the input image and initialize it to zeros.
```matlab
med_img     = zeros(size(img));
```

The algorithm of median filter is to simply apply the function to each pixel of the image. This can be done through iterating the entire pixels. Since an image is two dimensional, it would make sense to iterate it through nested loops.

Inside the second loop of the iteration, pixels around the selected pixel are used and then sorted to get its median. Once taken, set the return function value to the median.
```matlab
for row = 1:size(img, 1)
  for column = 1:size(img, 2)
    entire_row      = row:row+M-1;
    entire_column   = column:column+N-1;
    pixels          = padded_img(entire_row, entire_column);
    if mod(M*N, 2) == 0
      med_img(row, column)  = mean(sorted_pixels(M*N/2:M*N/2+1));
    else
      med_img(row, column)  = sorted_pixels((M*N+1)/2);
    end
  end
end
```

## 3 Results & Discussion
In this exercise, the function was tested on multiple image inputs with slight variations in the levels of salt and pepper noise in order to evaluate its effectiveness across different scenarios. The first image input is the default test image provided by the exercise module and it worked well as expected.

During the second image input test, it was observed that the input image was not in grayscale color space. However, the median filter function was still able to process the image by converting it from RGB color space to grayscale color space. The otuput of the image however is not an RGB color space but a grayscale color space.

The third input image is the same as the first one, but with an increased noise level from `0.02` to `0.2`. Despite using a `3x3 filter mask`, the median filter did not completely remove the salt and pepper noise from the output image. However, the filter performed even worse on the fourth image, which had a noise level closer to 1. The resulting output image was completely distorted, with no trace of the original input image left.

Input images and its output:
![[Pasted image 20230425193456.png]]
![[Pasted image 20230425193538.png]]
![[Pasted image 20230425194902.png]]
![[Pasted image 20230425195041.png]]

In the median filter parameter, setting the mask filter dimension to different values would result into a blurred image like the one shown below:
![[Pasted image 20230425200823.png]]
Notice that when the median filter mask is set to `1x1` dimension, there is no change or removal of the noise salt and pepper. 

The median filter fails at `0.2` noise level.

## 4 Comments & Conclusion
The purpose of this exercise is to eliminate the "salt and pepper" noise from input images using the median filter function. The function takes three parameters, namely the input image and the width and height of the filter mask. Modifying the dimensions of the mask can yield various output images, including ones with no discernible changes or images that appear excessively blurred.

The best configuration of the parameter for this code depends on the specific characteristics of the input image and the desired outcome. Generally, a larger filter size can remove more noise but can also result in a more blurred output image which can be seen from our sample input images. Smaller filter sizes, on the other hand, may not remove all the noise but can preserve more detail in the output image.

Based on the code, some of its limitations are:
1. It only supports 2D grayscale images. If the input image is in color or has more than two dimensions, the function will automatically convert it to grayscale using rgb2gray().
2. The function assumes that the salt and pepper noise is uniformly distributed across the image, and does not take into account the spatial characteristics of the noise.
3. The function employs a simple median filter with a fixed window size, which may not be effective for removing noise in all types of images or under different noise conditions.
4. The function does not provide any user interface for tuning the filter parameters or adjusting the noise removal algorithm.

There are several ways to further improve the output of the median filter:
1. Adjust the size of the filter mask: A larger filter mask may remove more noise, but at the cost of blurring the image. A smaller filter mask may preserve more detail but may not remove as much noise.
2. Use adaptive filtering: Instead of using a fixed filter mask size, adaptive filtering adjusts the size of the filter mask based on the local image properties. This can be more effective at removing noise while preserving detail.
3. Use other filtering techniques: Median filtering is just one type of filter that can be used to remove noise. Other filters such as Gaussian, bilateral, or Wiener filters may be more effective in some situations.
4. Use machine learning techniques: Machine learning algorithms can be used to learn the properties of noise in an image and remove it in a more sophisticated manner. However, this approach requires a large amount of training data and may be computationally expensive.
5. Use a combination of techniques: In practice, a combination of filtering techniques may be used to remove noise while preserving detail. For example, a median filter could be followed by a Gaussian filter to further smooth the image.

Note that *3*, *4*, and *5* are outside this exercise's scope.

# Exercise 1D – ( 3% ) – A "Smart" Edge Preserving Noise Filter
## 1 Background of the Problem
In this exercise, we are going to implemenet a smart edge preserving noise filter filter that smartly detects the edges of an input image using a Sobel filter. Using a simple blur will blur the entire image but with this exercise, edges are not blurred. This is achieved by reducing the proportion of the averaged image returned by the filter in areas of the image where the image gradients are large. 

## 2 Procedure
### Step 1
Create a blurred image B using a simple NxN averaging filter.
```matlab
B       = conv2(I, ones(N) / N^2, 'same');
```

Calculate the x and y image gradientsxI andyI using the following 5x5 Sobel gradient filters:
```matlab
Sobelx  = [ -4,   -5,   0,    5,    4; 
            -8,   -10,  0,    10,   8;
            -10,  -20,  0,    20,   10;
            -8,   -10,  0,    10,   8; 
            -4,   -5,   0,    5,    4];
Sobely  = [ 4,    8,    10,   8,    4; 
            5,    10,   20,   10,   5;
            0,    0,    0,    0,    0;
            -5,   -10,  -20,  -10,  -5; 
            -4,   -8,   -10,  -8,   -4];
Sobelx      = Sobelx*(1/240);
Sobely      = Sobely*(1/240);
```

Compute the gradient image G.
```matlab
Gradientx = conv2(I, Sobelx, 'same');
Gradienty = conv2(I, Sobely, 'same');
gradient_vector = sqrt(Gradientx.^2 + Gradienty.^2);
G = 7 * gradient_vector + 1;
```
The `7` here can be any number since it's simply an arbitraty constant that can be changed.

For each pixel, compute the weighting function W.
```matlab
W = ones(size(I));
```

For each pixel, construct the output image as a weighted combination of the blurred and original images using the computed weight values.
```matlab
for r = 1:size(I, 1)
    for c = 1:size(I, 2)
        if gradient_vector(r, c) <= tolerance
            W(r, c) = G(r, c) / tolerance;
        end
    end
end
```

## 3 Results & Discussion
The default image provided was used to test the smart blur function and the resulting output was nearly identical, as demonstrated below. This image has a default gaussian blur of `0.002`.
![[Pasted image 20230425220819.png]]

Increasing the gaussian blur to `0.02` reveals this result:
![[Pasted image 20230425220914.png]]

Further increasing it to `20%` would result to this:
![[Pasted image 20230425221008.png]]

The edge can still be seen however it is not that clear. The expected output of this smart blur image should show a very clear edge however what can be seen on the image above does not have a clear edge.

So far, that is for adjusting the tolerance level. If the `N` parameter value where to be set, like for example to 10, this would be the result shown below.
![[Pasted image 20230425221250.png]]
What this entails is that the image has been blurred a lot. Suffice to say, `N` represents the blur filter size.



## 4 Comments & Conclusion
This section of the assignment is quite difficult so I had an assistance by using an AI tool to help me develop the code so I am not that certain which configuration that provides the best output. The best parameter values to have a better result would depend on the image size as increasing `N` would increase its blur value and increasing `tolerance` would preserve more edges however it would create more noise. Basing on this scheme, it would be possible to have lower blur value and high tolerance intensity which would output a noisy image which we can then use to one of our exercise's median filter. This would probably fix the noise levels of the image.

There are several limitations to the smart blur function:
1. The code uses fixed Sobel filters of size 5x5, which may not be appropriate for all images. Different sizes and types of filters may be more suitable for different images.
2. The code does not provide a way to adjust the strength of the blur. The size of the blur is set by the input parameter N, but there is no way to control the strength of the blur separately from the size.
3. The code does not provide any options for adjusting the weighting between the original and blurred data. The weighting function is based solely on the gradient magnitude, and the tolerance level is used to determine when to switch between using the original and blurred data. There is no way to adjust the weighting function based on other criteria, such as image content or user preferences.
4. The code does not account for color images. It converts all input images to grayscale, which may not be appropriate for all applications.
5. The code is relatively slow due to the use of nested loops to compute the output image. This may be a limitation for large images or real-time applications.

Here are a few suggestions to improve the output of the smart blur function:
1. Fine-tune the N and tolerance values: The N and tolerance values determine the size of the blur filter and the threshold for detecting edges. Try experimenting with different values of N and tolerance to achieve the desired level of blur while preserving edge details.
2. Use a better edge detection algorithm: The Sobel filter used in this code is a simple edge detection algorithm that can produce jagged edges. Consider using more advanced algorithms like Canny edge detector or Hough transform to improve edge detection.
3. Use different weighting functions: The current weighting function is a linear function that only depends on the gradient magnitude. Try experimenting with other weighting functions that incorporate additional image features such as color or texture to achieve better results.
4. Apply the blur selectively: Instead of applying the blur uniformly across the entire image, try selectively applying the blur to specific regions of the image. For example, you could use a mask to apply the blur only to the noisy regions of the image while preserving the details in other areas.

# Exercise 1E– (2%) – Written Questions
**1. (1.0%) You have been given a set of imagery from a 256x256 pixel video surveillance camera to analyse. However, to work out roughly how far away objects of known size (eg. people) are from the camera in the footage you need to determine the field of view of the sensor. Using a tape measure as a guide you are able to estimate that a doorway of 2 metres height appears to span around 32 pixels in the imagery when viewed from 10 metres away.**
![[Pasted image 20230425224730.png]]

Q: Given the above, what is the likely field of view of the camera? *(you may assume the vertical and horizontal fields of view are the same)*
![[Pasted image 20230425230043.png]]


Q: How far away would a person of height 1.75 metres be if they appeared as  a region of height 8 pixels in this imagery?
![[Pasted image 20230425231515.png]]
If we ration the pixel of the door and the person, the person is 3.5x smaller in terms of pixels. Since we know it's 3.5x smaller, this would mean that the person is 3.5x away. Hence, if we multiply 10m by 3.5, the person is `35m` away from the camera.


**2. (1%) Carefully explain how a 'median' and an 'alpha trimmed mean' filter work and describe under what circumstances they are useful (illustrate if required).**
A median filter and an alpha trimmed mean filter are two types of nonlinear filters used to remove noise from images or signals.

A median filter works by replacing the intensity of each pixel with the median intensity value of its neighboring pixels (including itself). The median is calculated by sorting all the pixel intensities in the neighborhood from low to high and picking the middle value. This is useful for removing 'shot' or impulse noise while preserving edges.

An alpha trimmed mean filter works by removing a percentage (alpha) of the highest and lowest intensity pixels from the neighborhood, and then calculating the mean of the remaining pixels. The intensity of the center pixel is replaced with this mean. This filter is useful when there are extreme outlier pixels (high shot noise) that skew the mean. By trimming out these outliers, the filter can reduce the effect of shot noise while still smoothing the image.

For example, in a 5x5 neighborhood, if alpha is 0.2 (trim 20% of pixels), the top and bottom row (5 pixels) are removed. The mean is calculated from the remaining 15 central pixels. This makes the filter less sensitive to impulse noise compared to a standard mean filter.


Q: Without using a computer, what would be the result of applying a 3x3 and  a 5x5 median filter to the following simple image? *(you may assume that  white=1, black=0 and that all values outside the image boundaries shown  here are also black ie. 0)*
![[Pasted image 20230425232230.png]]


![[Pasted image 20230425234145.png]]
3x3 filter:
![[Pasted image 20230426000451.png]]
5x5 filter:
![[Pasted image 20230426000524.png]]


Q: Approximately, what would the result be if we instead applied a 3x3 alpha  trimmed mean filter with d=3 ?

![[Pasted image 20230426001527.png]]
Dark gray = 0.67
Light gray = 0.33

---
Github Reposity: [CMSC178 Assignment 1](https://github.com/KrulYuno/obsidian_files/tree/master/Codes)