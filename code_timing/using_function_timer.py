#!/usr/bin/env python3
"""
Example usage of function_timer.py
"""

from function_timer import timer


@timer
def check_membership(foo, bar):
    for i in foo:
        if i in bar:
            return True
    return False


@timer
def check_membership_faster(foo, bar):
    bar = set(bar)
    for i in foo:
        if i in bar:
            return True
    return False


def main():
    foo = [i for i in range(1000)]
    bar = [i for i in range(100000)]
    check_membership(foo, bar)
    check_membership_faster(foo, bar)

if __name__ == '__main__':
    main()
