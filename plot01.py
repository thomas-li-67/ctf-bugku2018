#!/usr/bin/python
# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import re

fn="temp/paint.txt"
#fn="temp/test.txt"
xl =[]
yl =[]
pattern = re.compile(r"\(([0-9]+),([0-9]+)\)")
with open(fn) as f:
    for line in f:
        m = pattern.search(line)
        if m != None:
            x = m.group(1)
            y = m.group(2)
            xl.append(int(x))
            yl.append(int(y))
            print x,y


#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(xl, yl,'o')       # Plot the sine of each x point
plt.show()                   # Display the plot