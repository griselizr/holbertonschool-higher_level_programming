#!/usr/bin/python3
"""
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """add two new lines to string"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    period = text.replace('.', '.\n\n')
    period = period.replace('?', '?\n\n')
    period = period.replace(':', ':\n\n')
    period1 = period.split('\n')
    for line in range(len(period1)):
        print("{}".format(period1[line].strip()),
              end=("" if (line == (len(period1) - 1)) else '\n'))
