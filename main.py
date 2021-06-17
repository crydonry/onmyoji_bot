import cv2
import numpy as np

from vision import Vision
from controller import Controller
from game import Game
from getFree import Getfree

vision = Vision()
controller = Controller()
#game = Game(vision, controller)
free = Getfree(vision, controller)

#screenshot = vision.get_image('xxxx.png')
#print(screenshot)
#match = vision.find_template('bible', image=screenshot , threshold=0.9)
#print(np.shape(match)[1])

free.run()
