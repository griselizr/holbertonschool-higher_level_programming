#!/usr/bin/python3
"""Creates a JSON file to read"""
import json


def load_from_json_file(filename):
    """Defie an object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
