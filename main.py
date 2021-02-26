from network_setup import enable_network
from deep_sleep import deep_sleep
from check_soil import test_soil

enable_network()
test_soil()
deep_sleep(100000)
