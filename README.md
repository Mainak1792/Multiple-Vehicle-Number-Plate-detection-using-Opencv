# Multiple-Vehicle-Number-Plate-detection-using-Opencv
 Here, the program detects multiple files from a directory and does image processing to extract the number in text format.
 The steps are as follows:
 1. From a directory of multiple images, detect single image as take it as a variable
 2. convert it to grayscale
 3. pass it through canny edge detection
 4. detect contour of specific area
 5. pass it through character recognition model
 6. extract the number in text format
 If the image processing doesnot detect any character I am converting it to 0000 . Thus any output which shows 0000 means, image processing is not able to extract the number plate.
