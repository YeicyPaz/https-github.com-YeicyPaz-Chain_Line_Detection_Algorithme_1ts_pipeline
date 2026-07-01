# Chain Line Extraction First Pipeline Algorithme
<big> This pipeline is the **first** approach of two approaches developed to extract string lines (also knows as Chain Lines) from manuscript images. The algorithm applies preprocessing to delete the text with the tool Magic Eraser, followed by adaptive binarization and the Hough Probabilistic Transform to draw lines.

However, this method has a lack of accuracy because the results vary according to the unique characteristics of each image, requiring manual adjustment of the parameters. </big>

If you want to test, it is necessary to make an adjustment in the **HoughLinesP function** area of the algorithm to obtain the best results in the images. (you will find it thanks to comments in the code)

The correct configuration to test each image you will see it below and the results in a online document:

### Image 1
  self.mean_lines = cv.HoughLinesP(
            self.mean_threshold, 1, np.pi/180, 80, minLineLength=500, maxLineGap=10   
### Image 2
  self.mean_lines = cv.HoughLinesP(
            self.mean_threshold, 1, np.pi/180, 60, minLineLength=400, maxLineGap=10

### Image 3
  self.mean_lines = cv.HoughLinesP(
            self.mean_threshold, 1, np.pi/180, 100, minLineLength=500, maxLineGap=15

### Image 4
  self.mean_lines = cv.HoughLinesP(
            self.mean_threshold, 1, np.pi/180, 80, minLineLength=500, maxLineGap=10
            
### Image 5
  self.mean_lines = cv.HoughLinesP(
            self.mean_threshold, 1, np.pi/180, 80, minLineLength=400, maxLineGap=10
         


## Document with results:
https://zenodo.org/records/21078831?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjMzY2M2ZTFmLTRmMzgtNGZlMC1iMTgyLTg3N2MzYzc3NmQxNSIsImRhdGEiOnt9LCJyYW5kb20iOiJiMTg2ZDM4ZjVkYWQ5ZTAwMmNiNDk4MzQ0YTJhZjNlNiJ9.s4-lOGhX4FPMc5ppi-N1Z53SITvSN6hg3wOut6RedfumPDuoV_aPL5mx5oUEzxi1TVDQ2auMjfMbTlI_RBFCSA 
