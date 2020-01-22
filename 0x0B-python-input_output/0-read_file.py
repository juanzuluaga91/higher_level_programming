#!/usr/bin/python3
""" Reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    with open(filename) as f:
        print(f.read(), end="")
