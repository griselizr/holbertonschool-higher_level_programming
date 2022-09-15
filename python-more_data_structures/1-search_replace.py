#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda rep : rep if rep != search else replace, my_list))
