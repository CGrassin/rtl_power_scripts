#! /usr/bin/env python

import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Plot a flattened CSV from rtl_power')
parser.add_argument('input_csv_file', help="rtl_power CSV file to process")
args = parser.parse_args()

x = []
y = []

for line in open(args.input_csv_file):
    line = line.strip().split(',')
    x.append(float(line[0]))
    y.append(float(line[1]))

plt.plot(x,y)
plt.show()