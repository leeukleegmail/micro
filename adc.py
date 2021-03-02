import time

from machine import I2C, Pin

from Adafruit_ADS1x15.ADS1x15 import ADS1115

i2c = I2C(scl=Pin(5), sda=Pin(4, Pin.PULL_UP), freq=100000)


def measure_value_adc():
    print("in measure")

    adc = ADS1115(i2c, address=119)

    while True:
        print("in while")
        value = adc.read()
        print('Channel 0: {0}'.format(value))
        # Sleep for half a second.
        time.sleep(1)
