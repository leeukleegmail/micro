from machine import Pin, ADC
import time

led = Pin(2, Pin.OUT)
moisture_lvl_analog = ADC(0)
moisture_lvl_digital = Pin(14, Pin.IN)
pump = Pin(12, Pin.OUT)
adc_power = Pin(13, Pin.OUT)


def water():
    led.value(1)
    print("Pump On")
    pump.on()
    time.sleep(2)
    print("Pump Off")
    pump.off()


def dont_water():
    print("Pump Off")
    led.value(0)
    pump.off()


def test_soil():
    adc_power.on()
    print("Moisture level digital is {}".format(moisture_lvl_digital.value()))
    print("Moisture level analog is {}".format(moisture_lvl_analog.read()))
    if moisture_lvl_analog.read() < 500:
        dont_water()
    else:
        water()
    adc_power.off()
    led.value(0)
