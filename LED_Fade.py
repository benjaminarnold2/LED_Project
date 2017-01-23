import pigpio
import time

pi = pigpio.pi()

red_pin = 17
green_pin = 22
blue_pin = 24


def colormath(color_setting, new_value, sleepytime):

    if color_setting < new_value:
        color_setting += 1
        #print(color_setting)
        time.sleep(sleepytime)
        return color_setting

    if color_setting > new_value:
        color_setting -= 1
        #print(color_setting)
        time.sleep(sleepytime)
        return color_setting


print("Set initial values:")

old_red_color = input("Set value for red:")
old_blue_color = input("Set value for blue:")
old_green_color = input("Set value for green:")

try:
    old_red_color = int(old_red_color)
    old_blue_color = int(old_blue_color)
    old_green_color = int(old_green_color)


except ValueError:

    print("I don't think that you gave me good numbers.")

pi.set_PWM_dutycycle(red_pin, old_red_color)
pi.set_PWM_dutycycle(blue_pin, old_blue_color)
pi.set_PWM_dutycycle(green_pin, old_green_color)

red_color = input("Set value for red:")
blue_color = input("Set value for blue:")
green_color = input("Set value for green:")

try:
    red_color = int(red_color)
    blue_color = int(blue_color)
    green_color = int(green_color)


except ValueError:

    print("I don't think that you gave me good numbers.")

count = 0

sleeptime = .003

while count < 256:

    old_red_color = colormath(old_red_color, red_color, sleeptime)
    pi.set_PWM_dutycycle(red_pin, old_red_color)

    old_blue_color = colormath(old_blue_color, blue_color, sleeptime)
    pi.set_PWM_dutycycle(blue_pin, old_blue_color)

    old_green_color = colormath(old_green_color, green_color, sleeptime)
    pi.set_PWM_dutycycle(green_pin, old_green_color)

    count += 1
