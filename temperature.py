import dht
from machine import Pin


def measure_temperature():
    d = dht.DHT22(Pin(4, Pin.IN, Pin.PULL_UP))
    print(d.measure())
    print(d.temperature())
    print(d.humidity())
