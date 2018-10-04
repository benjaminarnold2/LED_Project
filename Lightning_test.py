import pigpio
import time
from os import system
import random

system("sudo pigpiod")

pi = pigpio.pi()

red_pin = 17
green_pin = 22
blue_pin = 24

on_red_color = 255
on_blue_color = 255
on_green_color = 255

off_red_color = 0
off_blue_color = 0
off_green_color = 0


def light_on():

    print("on started")

    pi.set_PWM_dutycycle(red_pin, on_red_color)
    pi.set_PWM_dutycycle(blue_pin, on_blue_color)
    pi.set_PWM_dutycycle(green_pin, on_green_color)

    wait_time = random.uniform(.05, 3)
    time.sleep(wait_time)


def light_off():

    print("off started")
    pi.set_PWM_dutycycle(red_pin, off_red_color)
    pi.set_PWM_dutycycle(blue_pin, off_blue_color)
    pi.set_PWM_dutycycle(green_pin, off_green_color)

    wait_time = random.uniform(.05, 2)
    time.sleep(wait_time)


for x in range(0, 10):

    light_on()
    light_off()
