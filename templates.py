#!/usr/bin/python3
import sys


def arg_reciever():
    argv = sys.argv
    host = argv[1]
    args = argv[2:]
    return host, args


HOST, args = arg_reciever()

# rest of the code
