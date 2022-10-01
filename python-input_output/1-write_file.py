#!/usr/bin/python3
""" create a file to write"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
        filename (str): the file
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
