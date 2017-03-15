#!/usr/bin/env python3
"""
I use this script to time functions to better understand efficiency
USAGE:
    @timer
    def foo():
        do stuff
    foo()
"""
import time


def timer(function):
    def wrapper(*args):
        start = time.time()
        function(*args)
        stop = time.time()
        return stop - start
    return wrapper


def main():
    pass

if __name__ == '__main__':
    main()
