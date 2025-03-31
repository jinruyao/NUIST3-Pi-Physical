# Author: Jinru Yao
# Date: 2025-3-31

import RPi.GPIO as GPIO  	# Imports the RPi.GPIO library which allows interaction with the Raspberry Pi's GPIO pins [cite: 60, 61]
import time  			# Imports the time library, used for adding delays [cite: 62]
GPIO.setmode(GPIO.BCM)  	# Sets the GPIO pin numbering mode to BCM (Broadcom SOC channel) [cite: 63]
GPIO.setwarnings(False)  	# Disables GPIO warnings during the program execution
GPIO.setup(18, GPIO.OUT)  	# Sets GPIO pin 18 as an output pin
print("LED on")  		# Prints "LED on" to the terminal
GPIO.output(18, GPIO.HIGH)  	# Sets GPIO pin 18 to HIGH (3.3V), which turns the LED on [cite: 64, 65, 66]
time.sleep(1)  			# Pauses the program execution for 1 second [cite: 67]
print("LED off")  		# Prints "LED off" to the terminal
GPIO.output(18, GPIO.LOW)  	# Sets GPIO pin 18 to LOW (0V), which turns the LED off [cite: 68]
