import pigpio

pi = pigpio.pi()

red_pin = 17
green_pin = 22
blue_pin = 24


pi.set_PWM_dutycycle(red_pin, 0)
pi.set_PWM_dutycycle(blue_pin, 0)
pi.set_PWM_dutycycle(green_pin, 0)
