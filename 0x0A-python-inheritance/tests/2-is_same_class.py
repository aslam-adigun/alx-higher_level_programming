#!/usr/bin/python3
"""function that checks specified class and return boolean value"""

def is_same_class(obj, a_class):
    '''
    args:
       checks if the object is exactly an instance of the specified class.
       obj(value):The object to check.
       a_class(type):The class type of object
    Returns:
         If obj is exactly an instance of a_class - True.
         Otherwise - False.
    '''
    if type(obj) == a_class:
        return True
    return False
