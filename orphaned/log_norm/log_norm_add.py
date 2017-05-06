#!/usr/bin/env python3

"""
Script to normlize addresses in my rj-log.
"""

import csv
import geocoder
import re


def ext_apart(add):
    if re.search(r'([A][P][T] [\S]*)', add):
        match = re.search(r'([A][P][T] [\S]*)', add)
        match = match.group()
        match = f'APT:{match[3:]}'
        return match

    elif re.search(r'([A][P][T][:] [\S]*)', add):
        match = re.search(r'([A][P][T][:] [\S]*)', add)
        match = match.group()
        return match

    elif re.search(r'([#][\S]*)', add):
        match = re.search(r'([#][\S]*)', add)
        match = f'APT: {match.group()[1:]}'
        return match


def fix_add(add):
    add
    apt = ext_apart(add)
    g = geocoder.google(add)
    if apt:
        add = f'{g.housenumber} {g.street} {apt} {g.city}, {g.state} {g.postal}'
    else:
        add = f'{g.housenumber} {g.street} {g.city}, {g.state} {g.postal}'
    return add


def main():
    with open('logn.csv', 'r') as f:
        reader = csv.reader(f)
        data_in = list(reader)

    data_out = list()
    data_out.append(data_in[0])
    for line in data_in[1:]:
        line[10] = fix_add(line[10])
        data_out.append(line)

    with open('loga.csv', 'w+') as out:
            writer = csv.writer(out)
            writer.writerows(data_out)


if __name__ == '__main__':
    main()
