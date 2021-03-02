from adc import measure_value_adc
from check_soil import test_soil
from config import network_enabled, ifttt_enabled, sleep_after_measure, measure_soil, temperature_enabled
from deep_sleep import deep_sleep
from network_setup import enable_network
from send_ifttt_message import send_message
from temperature import measure_temperature

measurements = ""

if network_enabled:
    enable_network()
if measure_soil:
    measurements = test_soil()
if temperature_enabled:
    temperature = measure_temperature()
if ifttt_enabled:
    send_message(measurements)
if sleep_after_measure:
    deep_sleep(1000000)

print("in main")
measure_value_adc()
