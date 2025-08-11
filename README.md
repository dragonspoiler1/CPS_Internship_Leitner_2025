# CPS_Internship_2025_Leitner

# Goal
Further Work on the Project of my Predecessor as seen at https://github.com/Flo180/ev3_praktikum_projekt_griesser/tree/main

- Revamp the system that has been built and especiially improve on the communication between the EV3's.
- Add a Possibility to change configurations of the Machine during its runtime
- Add a Transporter that can bring the blocks that are sorted out to another Location
- Make a 3D Model/Render of the Build and Upload it here
- Learn and improve existing foundations
- Have fun

# Ressources used:



# Milestones and Completion
1.) Find a Way to let Bricks communicate with each other - Done (4.8)
2.) Setup all the Programms 
3.) Adjust Model





# Findings and Documentation
1.) The EV3 Bricks that are used do not have the ability to connect to WiFi even though there seems to be an option in its settings. With Reasearch of 
    its possibilites (Source: Getting started with LEGO® MINDSTORMS Education EV3 MicroPython Document will be listed) I Was able to come across the integrated "Messaging" function
    Messaging is a form of communication between Bricks using Bluetooth. 

  The setup is pretty simple in Theory, firstly you have to follow these steps:
  <img width="955" height="445" alt="image" src="https://github.com/user-attachments/assets/349cba85-c582-4f18-98b8-d5cf0c24426c" />
  <img width="941" height="579" alt="image" src="https://github.com/user-attachments/assets/98ef4a0c-2790-40c1-a86e-f83280a4f4e0" />

  Doing this with all your EV3's should do the Trick, note: The actuall connection part will happen in the Python files for now you just have to Pair them once.

  Now to the Code, I am using Visual Studio Code with the EV3 extension and pybrick libaries, most of the syntax is well documented and explained in the Manual.
  <img width="913" height="600" alt="image" src="https://github.com/user-attachments/assets/95454938-04de-4f8f-afb4-3c3605e57635" />

  As seen here, we have two Bricks, one acting as a Server, and the other as a Client. Throughout this Repository we will come across the term Box or Mailbox often
  these are quite suiting names for its purpose. There a different kinds of Mailboxes the difference in them being what kind of Data they allow to transmit. While the 
  Standard one communicates with Bytes something like the TextMailbox can transmit Strings as Informations. If Two or more Clients (and or Servers) share a Mailbox with 
  the same Name, they can read and send messages to one another using the read() and send() methods!

  Additonally we have methods like wait() that halts until the Mailbox is updated or new_wait() that does so until the Data gets updated to something that is not the current Value
  And then proceed

  With all that in Mind we can create complex Programs that can react to real life changes without even needing a wired connection.
  Further Documentation of the code will be commented in the Files 

  # Adjustmendts that were made:
  Changed the Color Sensor infront of the ELevator to a Ultrasonic Sensor that can Measure the Distance. This was made due to errors that can occure with color detextion and lightning.
  The Ultrasonic Sensor should give better results.

  Also Added a Touch Sensor at the Bottom of the Elevator to initialize the Motors and make sure to give a clean reset every time the Programm is started. Sets a Baseline (Note: could also function on a code        Basis if the Sensor Slot is needed via the run_until_stalled() method    )


  
      



# Author/Student
Nico Leitner
Student at HTL Leoben (3rd Year)
