#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, TouchSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

def middleButtonIsPressed(ev3):
    # Returns True if the center button of the EV3 brick is currently pressed.
    return Button.CENTER in ev3.buttons.pressed()

ev3 = EV3Brick()
COLORS = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
colorindex = 0




while True:
    if(middleButtonIsPressed(ev3) == True):
        if(colorindex >=3):
                colorindex = 0
        else:
                colorindex=colorindex+1
            
        ev3.screen.print(COLORS[colorindex])

    wait(500)