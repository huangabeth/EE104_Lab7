#heart rate of Aunlabelledtest__201108011113
#import packages
#pip install heartpy

import heartpy as hp
import matplotlib.pyplot as plt

sample_rate = 44100 #44.1kHz

# input data from csv file
data = hp.get_data('Aunlabelledtest__201108011113Draft2_Output_mono.csv')

# plot heart rate signal
plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()

#run analysis
wd, m = hp.process(data, sample_rate)

#visualise in plot to pinpoint peaks of heartbeats.
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#display computed time-domain measurements
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))