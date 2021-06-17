import numpy as np
import time

class Getfree:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
        self.state = 'not started'
    def run(self):
        while True:
            self.vision.refresh_frame()
            if self.state == 'not started' :
                self.log('game needs to be started')
                try:
                    self.state = 'started'
                except Exception as ex:
                    self.log('Failed to find bible')
            elif self.state == 'started' and self.found_bible():
                self.log('Found a bible, click_to_bible')
                try:
                    self.click_to_bible()
                    self.state = 'bible_done'
                except Exception as ex:
                    self.log('Failed to find bible')
            elif self.state == 'bible_done' and self.found_shop():
                self.log('Found a shop, click_to_shop')
                self.click_to_shop()
                self.state = 'shop_done'
            elif self.state == 'shop_done' and self.found_pack():    
                self.log('Found a pack, click_to_pack')
                self.click_to_pack()
                self.state = 'mission_finished'
            elif self.state == 'mission_finished' and self.found_close():    
                self.log('Found a close, click_to_close')
                self.click_to_close()
                self.state = 'mission_finished'
            elif self.state == 'mission_finished' and self.found_free():
                self.log('Found a free, click_to_free')
                self.click_to_free()
                self.state = 'started'
                break
            else:
                self.log('Not doing anything')
            time.sleep(1)

    def found_bible(self):
        matches = self.vision.find_template('bible', threshold=0.9)
        return np.shape(matches)[0] >= 1


    def click_to_bible(self):
        matches = self.vision.find_template('bible')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x+50, y+30)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def found_shop(self):
        matches = self.vision.find_template('shop', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def click_to_shop(self):
        matches = self.vision.find_template('shop')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def found_pack(self):
        matches = self.vision.find_template('pack', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def click_to_pack(self):
        matches = self.vision.find_template('pack')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def found_free(self):
        matches = self.vision.find_template('free', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def click_to_free(self):
        matches = self.vision.find_template('free')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(1)
        self.controller.left_mouse_click()
        time.sleep(0.5)
        
    def found_close(self):
        matches = self.vision.find_template('close', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def click_to_close(self):
        matches = self.vision.find_template('close')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)
        

    def log(self, text):
        print('[%s] %s' % (time.strftime('%H:%M:%S'), text))
