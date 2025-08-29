# CPS_Internship_2025_Leitner

# Goal

Further Work on the Project of my Predecessor as seen at <https://github.com/Flo180/ev3_praktikum_projekt_griesser/tree/main>

- Revamp the system that has been built and especiially improve on the communication between the EV3's.
- Track or keep count of the blocks in the system
- Add a Possibility to change configurations of the Machine during its runtime
- Learn and improve existing foundations
- Have fun

# Ressources used

4x Lego Mindstorms EV3
1x PixyCam V2 Lego Edition
 -> PixyMon Software
Build of Florian


# Milestones and Completion
1.) Find a Way to let Bricks communicate with each other
2.) Setup all the Programms 
3.) Adjust Model as needed
4.) Get it up and running
5.) Add/Change the build to ensure smooth running


# Findings and Documentation

1.) The EV3 Bricks that are used do not have the ability to connect to WiFi even though there seems to be an option in its settings. With some Reasearch I was able to come across the integrated "Messaging" 
function Messaging is a form of communication between Bricks using Bluetooth. 
    Sources: [Getting started with LEGO® MINDSTORMS Education EV3 MicroPython](https://pybricks.com/ev3-micropython/)

  The setup is pretty simple in Theory, firstly you have to follow these steps:
  <img width="951" height="746" alt="EV3Connection" src="https://github.com/user-attachments/assets/4b80fb22-af22-43fc-83c5-2241c21c08ee" />

  Doing this with all your EV3's should do the Trick, note: The actuall connection part will happen in the Python files, for now you just have to Pair them once.

  Now to the Code, I am using Visual Studio Code with the EV3 extension and pybrick libaries, most of the syntax is well documented and explained in the Manual.

  How does Communication work?
  <img width="880" height="644" alt="image" src="https://github.com/user-attachments/assets/a1387479-3b98-4673-be6e-377950f53655" />

  As seen here, we have two Bricks, one acting as a Server, and the other as a Client. Throughout this Repository we will come across the term Box or Mailbox often
  these are quite suiting names for its purpose. There a different kinds of Mailboxes the difference in them being what kind of Data they allow to transmit. While the
  Standard one communicates with Bytes something like the TextMailbox can transmit Strings as Informations. If Two or more Clients (and or Servers) share a Mailbox with
  the same Name, they can read and send messages to one another using the read() and send() methods!

  Additonally we have methods like wait() that halts until the Mailbox is updated or new_wait() that does so until the Data gets updated to something that is not the current Value
  And then proceed, note that this will make the process sleep till the condition is met

  Edit: To maintain a smoother cycle instead of making the process wait, I created a timer class that runs a process a short time period later. This was primarily done to ensure the Sorter and Elevator both '
  function with less interruption.

  After testing around with both a Colorsensor and an Ultrasonicsensor to determine Blocks infront of the Elevator, with both being too inaccurate and inconsistent towards detecting blocks on the Conveyor, it has
  been Replaced by a Camera.

  The one used here is the PixyCam V2 Lego Edition, a Camera with integrated Processors, a usable 640x400 Pixel Resolution and the ability for internal object detection. It can either be Plugged in via a Micro 
  USB to the Computer or ESP32 or with a EV3 Sensor Cable to said Unit. The setup isnt that difficult though you need the PixyMon Software for some configurations 
  (Link to Dowload: <https://pixycam.com/downloadspixy2/>)

  With the Help of these three articles/Guides it wasnt too difficult to build a reliable detection of Bricks passing through: 

  [General Infos about PixyCam]( <https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:pixymon_index>)
  
  [Getting into Object Detection](  <https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:teach_pixy_an_object_2> )
  
  [Accessing PixyCam in Micropython](https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:porting_guide)

  With all that in Mind we can create complex Programs that can react to real life changes without even needing a wired connection.

  Here is General Overview of the Programm:

  <img width="791" height="535" alt="image" src="https://github.com/user-attachments/assets/31aab063-9542-4dbb-8baa-e136d5fdf624" />



  After testing around with both a Colorsensor and an Ultrasonicsensor to determine Blocks infront of the Elevator, with both being too inaccurate and inconsistent towards detecting blocks on the Conveyor, it 
  has been Replaced by a Camera.

  The one used here is the PixyCam V2 Lego Edition, a Camera with integrated Processors, a usable 640x400 Pixel Resolution and the ability for internal object detection. It can either be Plugged in via a Micro 
  USB to the Computer or ESP32 or with a EV3 Sensor Cable to said Unit. The setup isnt that difficult though you need the PixyMon Software for some configurations (Link to Dowload: <https://pixycam.com/downloads-pixy2/>)

  With the Help of these two articles/Guides it wasnt too difficult to build a reliable detection of Bricks passing through: (General Infos about PixyCam: <https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:pixymon_index>
            Getting into Object Detection: <https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:teach_pixy_an_object_2>)

  Sadly some Sensors are miscalibrated or give faulty results which leads to some flaws



# Adjustmendts that were made

  Changed the Color Sensor infront of the Elevator to a Ultrasonic Sensor that can Measure the Distance. This was made due to errors that can occure with color detection and lighting.
  The Ultrasonic Sensor should give better results. After still getting misleading data switched to the PixyCamV2

  Also Added a Touch Sensor at the Bottom of the Elevator to initialize the Motors and make sure to give a clean reset every time the Programm is started. Sets a Baseline (Note: could also function on a code 
  Basis if the Sensor Slot is needed via the run_until_stalled() method which has been used instead)

# Author/Student

Nico Leitner
Student at HTL Leoben (3rd Year)
