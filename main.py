import numpy as np
import cv2 as cv
import os

class ManuscriptLineDetector:
    def __init__(self, file_path):
        """Initializes the detector, loads the image, and sets up base copies."""
        self.file_path = file_path
        self.original_image = cv.imread(file_path)
        assert self.original_image is not None, f"File could not be found: {file_path}"
        
        # Base copies for drawing results
        self.mean_image = self.original_image.copy()
        
        # Names for processed images 
        self.gray_image = None
        self.mean_threshold = None
        self.mean_lines = None

    def preprocess(self):
        """Applies grayscale, median blur, and adaptive threshold."""
        self.gray_image = cv.cvtColor(self.original_image, cv.COLOR_BGR2GRAY)
        self.gray_image = cv.medianBlur(self.gray_image, 5)

        # Binarization
        self.mean_threshold = cv.adaptiveThreshold(
            self.gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 45, 2
        )

    def detect_lines(self):
        """Uses HoughLinesP to detect lines."""
        
        self.mean_lines = cv.HoughLinesP(
            self.mean_threshold, 1, np.pi/180, 80, minLineLength=500, maxLineGap=10 #here are the parameters to change according to the initial result of the image,
             # in the readme document you can find the settings of parameters for each image that provide the best results
        )

    def filter_and_draw_lines(self):
        """Filters lines based on image orientation (height vs width) and draws them."""
        
        if self.mean_lines is None:
            print("No lines detected.")
            return

        # Calculate dimensions: shape returns (height, width, channels)
        height, width = self.original_image.shape[:2]
        
        # Determine orientation: True if portrait (taller), False if landscape (wider)
        is_portrait = height > width 
        
        
        for line in self.mean_lines:
            x1, y1, x2, y2 = line[0]
            
            dx = x2 - x1
            dy = y2 - y1
            
            angle_rad = np.arctan2(dy, dx)
            angle_degrees = np.degrees(angle_rad)
            absolute_angle = abs(angle_degrees)

            if is_portrait:
                # Vertical image -> Filter for VERTICAL LINES [85, 100]
                if 85 <= absolute_angle <= 100:
                    cv.line(self.mean_image, (x1, y1), (x2, y2), (0, 255, 0), 1, cv.LINE_AA)
            else:
                # Horizontal image -> Filter for HORIZONTAL LINES [0, 10] or [170, 180]
                if (0 <= absolute_angle <= 10) or (170 <= absolute_angle <= 180):
                    cv.line(self.mean_image, (x1, y1), (x2, y2), (0, 255, 0), 1, cv.LINE_AA)

    def show_results(self):
        """Displays the output windows."""
        #After processing the images, you will be able to see the original image in binary form and the original image with the lines detected
        cv.imshow("Binarization", self.mean_threshold)
        cv.imshow("Hough Lines", self.mean_image)
        
        cv.waitKey(0)
        cv.destroyAllWindows()

    def run(self):
        """Main execution flow."""
        self.preprocess()
        self.detect_lines()
        self.filter_and_draw_lines()
        self.show_results()

# --- Script Execution ---
if __name__ == "__main__":
    # Ensure to use raw string (r"") or forward slashes for Windows paths
    image_path = r"sans_letres_MAGIC_ERASER\5.JPG"
    
    detector = ManuscriptLineDetector(image_path)
    detector.run()