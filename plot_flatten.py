#! /usr/bin/env python

import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Plot a flattened CSV from rtl_power')
parser.add_argument('input_csv_file', help="rtl_power CSV file to process")
parser.add_argument("-t","--time", help="plot time-grouped file",action="store_true")
args = parser.parse_args()

x = []
y = []

for line in open(args.input_csv_file):
    line = line.strip().split(',')
    y.append(float(line[1]))

    if args.time:
        x.append(line[0])
    else:
        x.append(float(line[0]))
    
plt.plot(x,y)
plt.show()