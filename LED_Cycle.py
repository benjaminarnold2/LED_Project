import pigpio
import time

pi = pigpio.pi()

red_pin = 17
green_pin = 22
blue_pin = 24


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

print("Set first color values:")

one_red_color = input("Set value for red: ")
one_green_color = input("Set value for green: ")
one_blue_color = input("Set value for blue: ")


pi.set_PWM_dutycycle(red_pin, one_red_color)
pi.set_PWM_dutycycle(blue_pin, one_blue_color)
pi.set_PWM_dutycycle(green_pin, one_green_color)

print("Set second color values:")

two_red_color = input("Set value for red: ")
two_green_color = input("Set value for green: ")
two_blue_color = input("Set value for blue: ")


print("Set third color values:")

three_red_color = input("Set value for red: ")
three_green_color = input("Set value for green: ")
three_blue_color = input("Set value for blue: ")


sleeptime = input("Set fade time as .xx ")

while True:

    colorloop(one_red_color, one_blue_color, one_green_color, two_red_color,
              two_blue_color, two_green_color, sleeptime)

    colorloop(two_red_color, two_blue_color, two_green_color, three_red_color,
              three_blue_color, three_green_color, sleeptime)

    colorloop(three_red_color, three_blue_color, three_green_color, one_red_color,
              one_blue_color, one_green_color, sleeptime)

