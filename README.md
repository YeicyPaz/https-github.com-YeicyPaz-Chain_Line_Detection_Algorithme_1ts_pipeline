<big> This pipeline is the first approach developed to extract string lines from manuscript images. The algorithm applies preprocessing to delete the text (Magic Eraser), followed by adaptive binarization and the Hough Probabilistic Transform to draw lines.
However, this method has a lack of accuracy because the results vary according to the unique characteristics of each image, requiring manual adjustment of the parameters. </big>

if you want to test it is necessary to make an adjustment in the HoughLinesP area of the algorithm to obtain the best results in the images

