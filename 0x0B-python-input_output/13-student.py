#!/usr/bin/python3
"""
class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
"""


import os
import sys



class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        keys = self.__dict__.keys()
        values = self.__dict__.values()
        if type(attrs) == list:
            return dict(filter(lambda x: x[0] in attrs, zip(keys, values)))
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
