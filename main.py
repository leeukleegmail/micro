from check_soil import test_soil
from deep_sleep import deep_sleep
from network_setup import enable_network
from send_ifttt_message import send_message

enable_network()
measurements = test_soil()
send_message(measurements)
deep_sleep(100000)
