# Author: Jinru Yao
# Date: 2/4/2025

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red_led_pin = 18
green_led_pin = 17

GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)

# NUIST Quiz Game in Python
def quiz():
    print ("Welcome to the Animal Quiz!")
    print ("Answer the following questions:")

# Questions and Answers
    questions = [
        "1. Which of the following is NOT a python data type?: a. int, b. float, c. rational, d. string, e. bool ",
        "2. Which of the following is NOT a built-in operation in Python?: a. +, b. %, c. abs(), d. sqrt() ",
        "3. In a mixed-type expression involving ints and floats, Python will convert?: a. floats to ints, b. ints to strings, c. floats and ints to strings ",
        "4. The best structure for implementing a multi-way decision in Python is: a. if, b. if-else, c. if-elif-else, d. try ",
        "5. What statement can be executed in the body of a loop to cause it to terminate? a. if, b. exir, c. continue, d. break"
    ]
    answers = [
        "rational",
        "sqrt()",
        "ints to floats",
        "if-elif-else",
        "break"
    ]
    score = 0

# Ask questions
    for i in range(len(questions)):
        user_answer =  input(questions[i]).strip()
        if user_answer == answers[i]:
            print ("Correct!")
            score += 1
            # lighten the green light
            GPIO.output(green_led_pin, GPIO.HIGH)
            GPIO.output(red_led_pin, GPIO.LOW) # Make sure the red light is off
            time.sleep(0.5)  # green light will lighten for 0.5 second
            GPIO.output(green_led_pin, GPIO.LOW)
        else:
            print ("Incorrect!")
            # lighten the red light
            GPIO.output(red_led_pin, GPIO.HIGH)
            GPIO.output(green_led_pin, GPIO.LOW) # Make sure the green light is off
            time.sleep(0.5)  # red light will lighten for 0.5 second
            GPIO.output(red_led_pin, GPIO.LOW)

# Provide final score
    print ("\nQuiz completed!")
    print (f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
quiz()
