#!/usr/bin/python3
import sys


def arg_reciever():
    argv = sys.argv
    host = argv[1]
    submit_host = argv[2]
    args = argv[3:]
    return host, args


HOST, args = arg_reciever()

# rest of the code
