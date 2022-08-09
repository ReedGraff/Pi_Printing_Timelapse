# scp -r pi@192.168.2.80:~/Desktop/3D_Printer_Timelapse/Assets/ C:/Users/range/OneDrive/Desktop

import os


### Pi Board Initialization

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

### End of Pi Board Initialization



### Pi Camera Initialization

import picamera
import time
from time import sleep

#create object for PiCamera class
camera = picamera.PiCamera()
#set resolution
camera.resolution = (1024, 768)
camera.brightness = 60

### End of Pi Camera Initialization


Last_Photo = time.time() - 400

while True: # Run forever
    Current_Time = time.time()
    if (GPIO.input(10) == GPIO.LOW and Current_Time - Last_Photo >= 10): # If button is pressed
        print("Taking Photo")

        if (Current_Time - Last_Photo >= 400):
            print("Assuming new Print")

            dir_name = str(len(os.listdir("Assets/")))
            os.makedirs("Assets/" + dir_name + "_print")

            file_name = str(len(os.listdir("Assets/" + dir_name + "_print/")))
            camera.capture("Assets/" + dir_name + "_print/" + "image_" + file_name + ".jpeg")
            Last_Photo = time.time()

        else:
            print("Assuming new Print")
            dir_name = str(len(os.listdir("Assets/")) - 1)

            file_name = str(len(os.listdir("Assets/" + dir_name + "_print/")))
            camera.capture("Assets/" + dir_name + "_print/" + "image_" + file_name + ".jpeg")
            Last_Photo = time.time()