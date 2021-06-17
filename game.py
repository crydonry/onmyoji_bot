import numpy as np
import time

class Game:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
        self.state = 'not started'
        self.state_shop = 'not started'
    def run(self):
        while True:
            self.vision.refresh_frame()
            if self.state == 'not started':
                self.log('game needs to be started')
                self.state = 'started'
                self.state_shop = 'started'
            elif self.state == 'started' and self.state_shop == 'started' and self.found_bible():
                self.log('Found a bible, click_to_bible')
                self.click_to_bible()
                self.log('Found a bible, click_to_shop')
                self.click_to_shop()
                self.log('Found a bible, click_to_pack')
                self.click_to_pack()
                self.log('Found a bible, click_to_free')
                self.click_to_free()
                self.state_shop = 'not started'
            else:
                self.log('Not doing anything')
            time.sleep(1)

    def found_bible(self):
        matches = self.vision.find_template('bible', threshold=0.9)
        return np.shape(matches)[1] >= 1


    def click_to_bible(self):
        matches = self.vision.find_template('bible')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def click_to_shop(self):
        matches = self.vision.find_template('shop')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)
    def click_to_pack(self):
        matches = self.vision.find_template('pack')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)
    def click_to_free(self):
        matches = self.vision.find_template('free')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def log(self, text):
        print('[%s] %s' % (time.strftime('%H:%M:%S'), text))
