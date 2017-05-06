#!/usr/bin/env python3

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def open_dates():
    with open('dates.txt', 'r') as f:
        dates = f.readlines()
        dates = [date.strip() for date in dates]
        dates = [dt.datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
        return(dates)


def main():
    x = open_dates()
    y = range(len(x))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.plot(x, y)
    plt.ylabel('Referred Cases')
    plt.title('CRC Growth')
    plt.savefig('growth.png')


if __name__ == '__main__':
    main()
