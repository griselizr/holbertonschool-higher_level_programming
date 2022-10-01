#!/usr/bin/python3
""" Creates a JSON object txt file"""
import json


def from_json_string(my_str):
    """Return the JSON object txt"""
    return json.loads(my_str)
