import socket


def get_ip():
    """get current ip address"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("10.50.255.11", 80))
    current_ip = s.getsockname()[0]
    s.close()

    return current_ip
