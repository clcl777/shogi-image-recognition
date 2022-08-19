
import time

import pyautogui as pg
while True:
    time.sleep(1)
    #centers = pg.locateCenterAllOnScreen("kin.png", grayscale=True, confidence=0.6)
    centers = pg.locateAllOnScreen("kin.png", grayscale=True, confidence=0.9)
    #lst = list(centers)
    #print(len(lst))
    for center in centers:
        print(center)
    print("*****")
    
    '''
    center = pg.locateCenterOnScreen("kin.png", grayscale=True, confidence=0.6)
    print(center)  # Point(x=1504, y=128)
    '''
