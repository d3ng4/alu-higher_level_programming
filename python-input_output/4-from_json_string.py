#!/usr/bin/python3
"""
defines json to object functions
"""
import json


def from_json_string(my_str):
    """
    function that returns object representaion by json string
    """
    return (json.loads(my_str))
