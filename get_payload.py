import json


def payload():
    """use the data in config.json to get the payload"""
    with open('config.json', 'r') as f:
        data = json.load(f)

    username = data["username"]
    password = data["password"]
    isp = '@' + data["ISP"]
    ddddd = ',0,' + username + isp
    upass = password

    datas = {
        'DDDDD': ddddd,
        'upass': upass
    }

    return datas
