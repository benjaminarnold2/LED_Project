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


def colormath(color_setting, new_value, sleepytime):

    color_setting = int(color_setting)
    new_value = int(new_value)
    sleepytime = float(sleepytime)

    if color_setting < new_value:
        color_setting += 1
        # print(color_setting)
        time.sleep(sleepytime)
        return color_setting

    elif color_setting > new_value:
        color_setting -= 1
        # print(color_setting)
        time.sleep(sleepytime)
        return int(color_setting)

    else:

        return int(color_setting)


def light_on():

    # print("on started")
    pi.set_PWM_dutycycle(red_pin, on_red_color)
    pi.set_PWM_dutycycle(blue_pin, on_blue_color)
    pi.set_PWM_dutycycle(green_pin, on_green_color)

    wait_time = random.uniform(.05, 3)
    time.sleep(wait_time)


def light_off():

    # print("off started")
    pi.set_PWM_dutycycle(red_pin, off_red_color)
    pi.set_PWM_dutycycle(blue_pin, off_blue_color)
    pi.set_PWM_dutycycle(green_pin, off_green_color)

    wait_time = random.uniform(.05, 2)
    time.sleep(wait_time)


def lightning():

    for x in range(0, 10):
        light_on()
        light_off()


def colorloop(old_red_color, old_blue_color, old_green_color, red_color,
              blue_color, green_color, sleeptime):

    count = 0

    while count < 255:  # from one to two

        old_red_color = colormath(old_red_color, red_color, sleeptime)
        # print (old_red_color)
        pi.set_PWM_dutycycle(red_pin, old_red_color)

        old_blue_color = colormath(old_blue_color, blue_color, sleeptime)
        # print(old_blue_color)
        pi.set_PWM_dutycycle(blue_pin, old_blue_color)

        old_green_color = colormath(old_green_color, green_color, sleeptime)
        # print(old_green_color)
        pi.set_PWM_dutycycle(green_pin, old_green_color)

        count += 1

# print("Set first color values:")

# purple


one_red_color = 255
one_green_color = 0
one_blue_color = 255


pi.set_PWM_dutycycle(red_pin, one_red_color)
pi.set_PWM_dutycycle(blue_pin, one_blue_color)
pi.set_PWM_dutycycle(green_pin, one_green_color)

# print("Set second color values:")

# red
two_red_color = 255
two_green_color = 0
two_blue_color = 0


# print("Set third color values:")

# orange
three_red_color = 255
three_green_color = 105
three_blue_color = 0

# print("Set fourth color values:")

# green
four_red_color = 0
four_green_color = 255
four_blue_color = 0


sleeptime = .05

while True:

    colorloop(off_red_color, off_blue_color, off_green_color, one_red_color,
              one_blue_color, one_green_color, sleeptime)

    colorloop(one_red_color, one_blue_color, one_green_color, two_red_color,
              two_blue_color, two_green_color, sleeptime)

    colorloop(two_red_color, two_blue_color, two_green_color, three_red_color,
              three_blue_color, three_green_color, sleeptime)

    colorloop(three_red_color, three_blue_color, three_green_color, four_red_color,
              four_blue_color, four_green_color, sleeptime)

    colorloop(four_red_color, four_blue_color, four_green_color, off_red_color,
              off_blue_color, off_green_color, sleeptime)

    lightning()
