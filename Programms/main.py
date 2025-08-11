#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick

from pybricks.ev3devices import *
from pybricks.parameters import Port
from pybricks.tools import wait


from pybricks.messaging import BluetoothMailboxClient, TextMailbox

#This Section intends the Conveyor to be controlled by a single EV3 Brick
#Might get changed later to not waste additional ressources current limiting factor is cable length

ev3 = EV3Brick()
ultraS = UltrasonicSensor(Port.S2)

while True:
    print(ultraS.distance())
    wait(100)