from machine import Pin, I2C
import BME280

i2c = I2C(scl=Pin(5), sda=Pin(4, Pin.PULL_UP), freq=100000)
bme = BME280.BME280(i2c=i2c, address=119)


def measure_temperature():
    return bme.temperature
