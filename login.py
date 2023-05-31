import get_payload
import requests
import socket


def get_ip():
    """get current ip address"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("10.50.255.11", 80))
    current_ip = s.getsockname()[0]
    s.close()

    return current_ip


def login():
    """get the request url """
    url = "http://10.50.255.11:801/eportal/"
    current_ip = get_ip()
    params = {
        'c': 'ACSetting',
        'a': 'Login',
        'protol': 'http',
        'hostname': '10.50.225.11',
        'iTermType': 1,
        'wlanuserip': current_ip,
        'wlanacip': 'null',
        'wlanacname': 'me60',
        'mac': '00-00-00-00-00-00',
        'ip': current_ip,
        'enAdvert': 0,
        'queryACIP': 0,
        'jsVersion': '2.4.3',
        'loginMethod': 1
    }

    payload = get_payload.payload()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'}

    r = requests.post(url, data=payload, params=params, headers=headers, allow_redirects=False)
    # the redirect must be disabled, or it will be redirected to a wrong url
