#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, BluetoothMailboxClient, TextMailbox


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port


def get_color_name(color_sensor):
    
    # Get the detected color (returns a color object)
    detected_color = color_sensor.color()
    
    # Map color IDs to English names
    color_names = {
        0: "No color",    # Color.BLACK (sometimes ambient light)
        1: "Black",       # Color.BLACK (when close to surface)
        2: "Blue",        # Color.BLUE
        3: "Green",       # Color.GREEN
        4: "Yellow",      # Color.YELLOW
        5: "Red",         # Color.RED
        6: "White",      # Color.WHITE
        7: "Brown",       # Color.BROWN
        None: "Unknown"  # If no color detected
    }
    
    return color_names.get(detected_color, "Unknown")

# initializing
ev3 = EV3Brick()
client = BluetoothMailboxClient()
mbox = TextMailbox('CurrentColor',client)
color_sensor = ColorSensor(Port.S1)

client.connect('ev3dev')
ev3.speaker.say("connected")

ev3.screen.print("Sending Message!")
mbox.send('Hello World')
ev3.screen.print("Message sent!")

mbox.wait()
ev3.screen.print("Received a new Message: ")
ev3.screen.print(mbox.read())

ev3.speaker.beep()
ev3.speaker.beep()

while True: 
    mbox.send(color_sensor.color())
    wait(1000)

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, BluetoothMailboxClient, TextMailbox


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port


def get_color_name(color_sensor):
    
    # Get the detected color (returns a color object)
    detected_color = color_sensor.color()
    
    # Map color IDs to English names
    color_names = {
        0: "No color",    # Color.BLACK (sometimes ambient light)
        1: "Black",       # Color.BLACK (when close to surface)
        2: "Blue",        # Color.BLUE
        3: "Green",       # Color.GREEN
        4: "Yellow",      # Color.YELLOW
        5: "Red",         # Color.RED
        6: "White",      # Color.WHITE
        7: "Brown",       # Color.BROWN
        None: "Unknown"  # If no color detected
    }
    
    return color_names.get(detected_color, "Unknown")

# initializing
ev3 = EV3Brick()
client = BluetoothMailboxClient()
mbox = TextMailbox('CurrentColor',client)
color_sensor = ColorSensor(Port.S1)

client.connect('ev3dev')
ev3.speaker.say("connected")

ev3.screen.print("Sending Message!")
mbox.send('Hello World')
ev3.screen.print("Message sent!")

mbox.wait()
ev3.screen.print("Received a new Message: ")
ev3.screen.print(mbox.read())

ev3.speaker.beep()
ev3.speaker.beep()

while True: 
    mbox.send(color_sensor.color())
    wait(1000)

