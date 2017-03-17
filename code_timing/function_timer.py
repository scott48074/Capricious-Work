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
    message = '{}\n{}() Processed for {}\n{}'

    def wrapper(*args):
        start = time.time()
        results = function(*args)
        stop = time.time()
        print(message.format('=' * 82, function.__name__, stop - start, '=' * 82))
        return results
    return wrapper


def main():
    pass

if __name__ == '__main__':
    main()
