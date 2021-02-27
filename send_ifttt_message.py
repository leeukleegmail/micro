import urequests as urequests

import config

ifttt_url = 'http://maker.ifttt.com/trigger/{}/with/key/{}'


def send_message(sensor_readings):
    request_headers = {'Content-Type': 'application/json'}
    request = urequests.post(ifttt_url.format(config.ifttt_webhook_name, config.ifttt_api_key),
                             json=sensor_readings,
                             headers=request_headers)
    print(request.text)
    request.close()
