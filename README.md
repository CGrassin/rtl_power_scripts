# Scripts for rtl_power 

This repository contains a suite of simple Python scripts to use the output of the RTL-SDR `rtl_power` command (mostly for radio astronomy in my case). All scripts are independant and their usage and output are detailed below.

## heatmap.py

**Purpose:** to draw a waterfall chart from `rtl_power` data. Original script for [keenerd](https://github.com/keenerd/rtl-sdr-misc).

**Usage:** basic usage `python heatmap.py input_file.csv output.png`, call `python heatmap.py -h` for arguments breakdown.

<!-- **Output:** -->

## flatten.py

**Purpose:** to convert the output of `rtl_power` to a 1D CSV file (grouping by frequency or time). Original script for [keenerd](https://github.com/keenerd/rtl-sdr-misc).

**Usage:** basic usage `python flatten.py input_file.csv > input_file_1D.csv`, call `python flatten.py -h` for arguments breakdown.

<!-- **Output:** -->

## plot_flatten.py

**Purpose:** to plot a flattened csv file.

**Usage:** basic usage `python plot_flatten.py input_file_1D.csv`.

<!-- **Output:** -->