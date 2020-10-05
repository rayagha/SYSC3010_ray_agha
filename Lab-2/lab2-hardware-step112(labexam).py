from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def letterT():
    P = yellow
    O = nothing
    logo = [
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, P, P, O, O, O,
    ]
    return logo

def letterA():
    P = yellow
    O = nothing
    logo = [
    O, O, P, P, P, P, O, O,
    O, P, P, P, P, P, P, O,
    O, P, P, O, O, P, P, O,
    O, P, P, O, O, P, P, O,
    O, P, P, P, P, P, P, O,
    O, P, P, P, P, P, P, O,
    O, P, P, O, O, P, P, O,
    O, P, P, O, O, P, P, O,
    ]
    return logo

images = [letterT,letterA,letterT, letterA]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
    
s.clear()