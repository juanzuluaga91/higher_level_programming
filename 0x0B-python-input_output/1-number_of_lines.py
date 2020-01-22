#!/usr/bin/python3
""" Reads n lines of a text file (UTF8) and prints it to stdout """


def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        lines = sum(1 for line in f)
    f.closed
    return lines
