#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.ev3devices import Motor

ev3 = EV3Brick()
motorA = Motor(Port.A)
motorB = Motor(Port.B)


motorA.run(160)
motorB.run(160)