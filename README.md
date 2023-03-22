# Spot-Micro-Control-and-Animation
Inverse Kinematics based control and animation of Spotmicro developped in Python for Raspeberry Pi

This first version is a "simulator" of Spot Micro that runs under Python 3 and requires the Pygame Library in order to display animation and use the xbox one (or any similar) controller. I developped it with on a Raspberry Pi 4 but it runs successfully also on a Windows 10 PC.

I attached a pdf file that gives some details about how inverse kinematics is built-up and correspondance between calculated angles and servos angles.

Attached Libraries:

* Spotmicro_Inverse_Kinematics_and_Position_Library_v01.py: This file contains a class of paramaters and functions to calculate Spot micro position. It includes:
  
   -The main dimensions of Spot micro
   
   -The center of gravity position and weight of each spotmicro limbs and body
   
   -The forward kinematics function
   
   -The forward kinematics functions
   
   -The function that generates walking positions
   
   -The function that generates positions from known start and end positionsThis library contains a class of functions to calculate the center of gravity position
    and distance to the support polygon edge


* Spotmicro_Gravity_Center_Library_v01.py: This file contains a class of functions to calculate the center of gravity position and distance to the support polygon edge


* Spotmicro_Animation_Library_v01.py:
  This file contains a class of functions to generate the animation frames

Please make sure that all these files are located in the same folder.

* Essai_Joystick_01.py: This utility was copied from https://www.pygame.org/docs/ref/joystick.html. It is helpfull to identify the controller / joystick parameters


My own Spot Micro version uses:

-Raspberry Pi 3n

-PCA9685 shield (I2c) 

-12 x 11 kg.cm servos

-2 HC-SR04 untrasonic range sensors

-20 A SBEC supply (servos) set at 6V

-5 A 5v power supply for the raspberry pi

-old laptop charger for power

I hope you will enjoy playing with this software and build-up your own walking Spot Micro ! 

Originally written by 
Arnaud Villeneuve

December 2020




