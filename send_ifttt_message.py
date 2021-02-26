import urequests as urequests

import credentials

url = 'http://maker.ifttt.com/trigger/{}/with/key/{}'


def send_message(sensor_readings):
    request_headers = {'Content-Type': 'application/json'}

    request = urequests.post(url.format(credentials.ifttt_webhook_name, credentials.ifttt_api_key),
                             json=sensor_readings,
                             headers=request_headers)
    print(request.text)
    request.close()
