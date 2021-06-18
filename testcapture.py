import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Onmyoji')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    #cv.imshow('Computer Vision', screenshot)
    

    # debug the loop rate
    #loop_time = time()

    gray = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    template = cv.imread('img/CHALLENGE.png',0)

    # run template matching, get minimum val
    res = cv.matchTemplate(gray, template, cv.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    # create threshold from min val, find where sqdiff is less than thresh
    min_thresh = (min_val + 1e-6) * 1.5
    match_locations = np.where(res<=min_thresh)

    # draw template match boxes
    w, h = template.shape[::-1]
    for (x, y) in zip(match_locations[1], match_locations[0]):
        cv.rectangle(screenshot, (x, y), (x+w, y+h), [0,255,255], 2)

    # display result
    cv.imshow('', screenshot)
    cv.waitKey(5)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
