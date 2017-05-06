#!/usr/bin/env python

"""
A Quick script to sort and format a list of names
"""
FILE = '/home/scott/Scripts/Capricious-Work/rj_list_sort/my-referrals.txt'


def fix(name):
    name = name.replace('_', ' ')
    name_list = name.split(' ')
    name_list = [part.title() for part in name_list]
    if len(name_list) == 3:
        name_list = [name_list[1], name_list[2], name_list[0]]
    elif len(name_list) == 2:
        name_list = reversed(name_list)

    name = ', '.join(name_list)
    return name


def main():
    with open(FILE, 'r') as names:
        fixed = [fix(name.strip()) for name in names]
        fixed.sort()

    with open('out.txt', 'w+') as out:
        for name in fixed:
            out.write(name + '\n')


if __name__ == "__main__":
    main()
