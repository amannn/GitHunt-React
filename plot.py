#!/usr/bin/env python

import matplotlib.pyplot as plt
import json

statsFile = open('stats.json', 'r')
heapSizes = json.load(statsFile)

plt.plot(heapSizes)
plt.ylabel('Heap Size')
plt.show()
