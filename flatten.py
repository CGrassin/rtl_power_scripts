#! /usr/bin/env python

import argparse
from collections import defaultdict

# todo:
# frequency bins
# header line
# time

parser = argparse.ArgumentParser(description='Turns any rtl_power csv into a more compact summary')
parser.add_argument('input_csv_file', help="rtl_power CSV file to process")
parser.add_argument("-t","--time", help="group by time instead of frequency",action="store_true")
args = parser.parse_args()

path = args.input_csv_file

def frange(start, stop, step):
    i = 0
    f = start
    while f <= stop:
        f = start + step*i
        yield f
        i += 1

sums = defaultdict(float)
counts = defaultdict(int)

for line in open(path):
    line = line.strip().split(', ')
    date = str(line[0])
    time = str(line[1])
    low = int(line[2])
    high = int(line[3])
    step = float(line[4])
    weight = int(line[5])
    dbm = [float(d) for d in line[6:]]
    for f,d in zip(frange(low, high, step), dbm):
        key = time if args.time else f
        sums[key] += d*weight
        counts[key] += weight
        
ave = defaultdict(float)
for f in sums:
    ave[f] = sums[f] / counts[f]

for f in sorted(ave):
    print(','.join([str(f), str(ave[f])]))