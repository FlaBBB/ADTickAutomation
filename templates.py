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
