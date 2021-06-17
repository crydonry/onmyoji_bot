import json
import logging
import random
import time


class Mood:
    '''
    Used to simulate the clicking frequency of random, change a click rules every 5 minutes \ n
    Energetic: excellent state, click delay at 1-1.5s \ n
    Joyful: State is good, click delay in 1.3-2.1s \ n
    Normal: Status, click latency at 1.8-3S \ n
    Tired: Status fatigue, click delay in 2.5-4 \ n
    Exhausted: Chsm, click latency at 3-5s \ n
    '''
    __first_init = True

    def __init__(self, state=5):
        self.lastime = time.time()
        self.state = state
        if Mood.__first_init:
            self.read_config()
            Mood.__first_init = False
        a = random.randint(1, self.state)
        logging.info("Create a delay parameter，grade: %d", a)
        self.lastmood = Mood.mymood[a]

    def read_config(self):
        try:
            # Read delay configuration
            with open('delay.json', 'r') as f:
                fileObject = f.read()
            jsObj = json.loads(fileObject)
            logging.info('Read the delay configuration file success')
            Mood.mymood = {
                1: (jsObj['1'][0], jsObj['1'][1]),
                2: (jsObj['2'][0], jsObj['2'][1]),
                3: (jsObj['3'][0], jsObj['3'][1]),
                4: (jsObj['4'][0], jsObj['4'][1]),
                5: (jsObj['5'][0], jsObj['5'][1])}
        except FileNotFoundError:
            # file not found
            logging.info('Use the default delay parameters')
            self.set_default()
        except:
            # Other errors
            logging.warning('Delay profile error, use the default parameters')
            self.set_default()
        logging.info('Delay parameter: '+str(Mood.mymood))

    def set_default(self):
        '''
        Set default delay parameters
        '''
        Mood.mymood = {
            1: (1000, 500),
            2: (1300, 800),
            3: (1800, 1200),
            4: (2500, 1500),
            5: (3000, 2000)}

    def getmood(self):
        if (time.time() - self.lastime >= 300):
            self.lastime = time.time()
            a = random.randint(1, self.state)
            self.lastmood = Mood.mymood[a]
            logging.info("Modify delay parameters, level %d", a)
        return self.lastmood

    def moodsleep(self):
        mysleep(*self.getmood())

    def get1mood(self):
        return random.randint(self.getmood()[0], self.getmood()[0] + self.getmood()[1])


def firstposition():
    '''
    Get click position, deduct the soul of the soul
        : Return: Return Random Position Coordinate
    '''
    safe_area = {
        1: ((20, 106), (211, 552)),
        2: ((931, 60), (1120, 620))}

    index = random.randint(1, 2)
    return safe_area[index]


def secondposition():
    '''
    Get click position, deduct the soul of the soul
        : Return: Return Random Position Coordinate
    '''
    return (random.randint(970, 1111), random.randint(100, 452))


def checkposition(pos):
    '''
    Calibrated settlement position
        : Param Pos: (X, Y) position coordinates
        : Return: Return False if the right returns True, otherwise
    '''
    if pos[0] < 1111 and pos[0] > 970:
        if pos[1] < 452 and pos[1] > 100:
            return True
    return False


def mysleep(slpa, slpb=0):
    '''
    randomly sleep for a short time between `slpa` and `slpa + slpb` \n
    because of the legacy reason, slpa and slpb are in millisecond
    '''
    if slpb == 0:
        slp = random.randint(int(0.5*slpa), int(1.5*slpa))
    else:
        slp = random.randint(slpa, slpa+slpb)
    time.sleep(slp/1000)


if __name__ == "__main__":
    mood = Mood()
    print(Mood.mymood)
