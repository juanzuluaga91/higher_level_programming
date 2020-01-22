#!/usr/bin/python3
""" Reads n lines of a text file (UTF8) and prints it to stdout """


def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for i in range(0, nb_lines):
                print(f.readline(), end="")
