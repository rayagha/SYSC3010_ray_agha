from sense_hat import SenseHat
import time

s = SenseHat()
s.clear()
"""
h = s.get_humidity()
s.show_message("Humidity: %d%%" %h, text_colour = [255, 0, 0])
time.sleep(3)

t = s.get_temperature()
s.show_message("Temperature: %dC" %t, text_colour = [0, 255, 0])
time.sleep(3)

p = s.get_pressure()
s.show_message("Pressure: %dMillibars" %p, text_colour = [0, 0, 255])
time.sleep(3)

"""
co = 23

def eman():
    nm = ""
    if(co%2==0):
        nm = "R"
        
    if(co%2!=0):
        nm = "A"
        
    return nm
    


def left():
    ++co
    s.show_message("<")
    time.sleep(1)
    s.show_message (eman())
    
  
    
def right():
    s.show_message(">")
    time.sleep(1)
    s.show_message (eman())
    
def up():
    s.show_message("up")
    time.sleep(1)
    s.show_message (eman())
    
def down():
    s.show_message("v")
    time.sleep(1)
    s.show_message (eman())
  
s.stick.direction_left = left
s.stick.direction_right = right
s.stick.direction_up = up
s.stick.direction_down = down
