import time

from machine import Pin, ADC

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
    time.sleep(2)
    actual_moisture_level_analog = moisture_lvl_analog.read()

    print("Moisture level digital is {}".format(moisture_lvl_digital.value()))
    print("Moisture level analog is {}".format(actual_moisture_level_analog))
    
    if actual_moisture_level_analog < 500:
        dont_water()
        outcome = "Not Watered"
    else:
        water()
        outcome = "Watered"

    adc_power.off()
    led.value(0)
    return {'value1': actual_moisture_level_analog, 'value2': outcome}
