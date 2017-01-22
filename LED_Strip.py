import pigpio


pi = pigpio.pi()

RED = 17
GREEN = 22
BLUE = 24

while True:

    color = input("What color would you like to change? ")

    brightness = input("How bright do you want that color? ")

    if color == "red":

        print (color)
        print (brightness)
        pi.set_PWM_dutycycle(RED, brightness)

    elif color == "green":

        print (color)
        print (brightness)
        pi.set_PWM_dutycycle(GREEN, brightness)

    elif color == "blue":

        print (color)
        print (brightness)
        pi.set_PWM_dutycycle(BLUE, brightness)

    else:

        print ("Please try again.")

