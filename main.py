"""utf-8 code """

import requests
from bs4 import BeautifulSoup
import login


def check():
    """check the login status"""
    url = 'http://10.50.255.11'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    if soup.title.string == '注销页':
        return True
    else:
        return False


if __name__ == '__main__':
    if check():
        print("You have logged in")
    else:
        login.login()
        if check():
            print("Successfully!")
        else:
            print("Login failed!")
