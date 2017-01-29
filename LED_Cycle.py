import pigpio
import time

pi = pigpio.pi()

red_pin = 17
green_pin = 22
blue_pin = 24

count = 0

sleeptime = .003


def colormath(color_setting, new_value, sleepytime):

    color_setting = int(color_setting)
    new_value = int(new_value)

    if color_setting < new_value:
        color_setting += 1
        # print(color_setting)
        time.sleep(sleepytime)
        return color_setting

    if color_setting > new_value:
        color_setting -= 1
        # print(color_setting)
        time.sleep(sleepytime)
        return color_setting

print("Set first color values:")

one_red_color = input("Set value for red:")
one_blue_color = input("Set value for blue:")
one_green_color = input("Set value for green:")

pi.set_PWM_dutycycle(red_pin, one_red_color)
pi.set_PWM_dutycycle(blue_pin, one_blue_color)
pi.set_PWM_dutycycle(green_pin, one_green_color)

print("Set second color values:")

two_red_color = input("Set value for red:")
two_blue_color = input("Set value for blue:")
two_green_color = input("Set value for green:")

print("Set third color values:")

three_red_color = input("Set value for red:")
three_blue_color = input("Set value for blue:")
three_green_color = input("Set value for green:")

while True:

    old_red_color = one_red_color
    old_blue_color = one_blue_color
    old_green_color = one_green_color

    red_color = two_red_color
    blue_color = two_blue_color
    green_color = two_green_color

    while count < 256:  # from one to two

        old_red_color = colormath(old_red_color, red_color, sleeptime)
        old_red_color = str(old_red_color)
        pi.set_PWM_dutycycle(red_pin, old_red_color)

        old_blue_color = colormath(old_blue_color, blue_color, sleeptime)
        old_blue_color = str(old_blue_color)
        pi.set_PWM_dutycycle(blue_pin, old_blue_color)

        old_green_color = colormath(old_green_color, green_color, sleeptime)
        old_green_color = str(old_green_color)
        pi.set_PWM_dutycycle(green_pin, old_green_color)

        count += 1

    red_color = three_red_color
    blue_color = three_blue_color
    green_color = three_green_color

    count = 0

    while count < 256:  # from two to three

        old_red_color = colormath(old_red_color, red_color, sleeptime)
        old_red_color = str(old_red_color)
        pi.set_PWM_dutycycle(red_pin, old_red_color)

        old_blue_color = colormath(old_blue_color, blue_color, sleeptime)
        old_blue_color = str(old_blue_color)
        pi.set_PWM_dutycycle(blue_pin, old_blue_color)

        old_green_color = colormath(old_green_color, green_color, sleeptime)
        old_green_color = str(old_green_color)
        pi.set_PWM_dutycycle(green_pin, old_green_color)

        count += 1

    red_color = three_red_color
    blue_color = three_blue_color
    green_color = three_green_color

    count = 0

    while count < 256:  # from three to one

        old_red_color = colormath(old_red_color, red_color, sleeptime)
        old_red_color = str(old_red_color)
        pi.set_PWM_dutycycle(red_pin, old_red_color)

        old_blue_color = colormath(old_blue_color, blue_color, sleeptime)
        old_blue_color = str(old_blue_color)
        pi.set_PWM_dutycycle(blue_pin, old_blue_color)

        old_green_color = colormath(old_green_color, green_color, sleeptime)
        old_green_color = str(old_green_color)
        pi.set_PWM_dutycycle(green_pin, old_green_color)

        count += 1

    count = 0
