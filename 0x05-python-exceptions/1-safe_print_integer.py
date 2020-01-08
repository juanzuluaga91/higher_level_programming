#!/usr/bin/python3
def safe_print_integer(v):
    try:
        print("{:d}".format(v))
    except:
        return (False)
    return (True)
