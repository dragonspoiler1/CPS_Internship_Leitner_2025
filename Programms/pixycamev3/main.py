#!/usr/bin/env pybricks-micropython
from pixy2 import Pixy2 
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()
pixycam2 = Pixy2(port=4,i2c_address=0x54)

# Extract data of first (and only) block 
while True:
    pixycam2.get_blocks(10,1)
    nr_blocks, blocks = pixycam2.get_blocks(1, 1)
    if (nr_blocks >= 1):
        ev3.speaker.beep()
        
    wait(100)
