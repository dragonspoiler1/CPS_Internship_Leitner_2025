#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, TouchSensor, UltrasonicSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from utime import ticks_ms, ticks_diff


ev3 = EV3Brick()

sorterMotor = Motor(Port.B)
sorterColorSensor = ColorSensor(Port.S3)
colorToBeFiltered = Color.BLUE

liftMotor = Motor(Port.A)

while True:
    color = sorterColorSensor.color()
    if (color == colorToBeFiltered and not None):
        print(color)
        
    wait(100)