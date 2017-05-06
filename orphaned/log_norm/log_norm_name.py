#!/usr/bin/env python3

"""
Script to normalize my rj-log data.
"""

import csv


def fix_name(name):
    name = name.split()
    name = [part.strip().title() for part in name]
    if len(name) is 1:
        name = ['First', 'Middle', 'Last', 'Title']
    elif len(name) is 2:
        name = [name[0], '', name[1], '']
    elif len(name) is 3:
        name = [name[0], name[1], name[2], '']
    return name


def main():
    with open('log.csv', 'r') as f:
        reader = csv.reader(f)
        data_in = list(reader)
    data_out = []
    for line in data_in:
        name = fix_name(line[3])
        data_out.append(line[:3] + name[:] + line[4:])

    with open('logn.csv', 'w+') as out:
        writer = csv.writer(out)
        writer.writerows(data_out)


if __name__ == '__main__':
    main()
