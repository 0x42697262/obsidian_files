function Iblur = blur_image(I,B)
Iblur = conv2(I,B,'same');
return