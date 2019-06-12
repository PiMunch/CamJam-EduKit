# needs w1thermsensor [sudo apt install python3-w1thermsensor]

import matplotlib.pyplot as plt
#import numpy as np
import matplotlib.patches as mpatches
from time import sleep
from w1thermsensor import W1ThermSensor
from gpiozero import LED

sensor = W1ThermSensor()

temp_list = []
x = []
a = 0
temp = 0
red = LED(12)
red.off()
trigger_threshold = 25

#SET-UP GRAPH
plt.ion()
fig, ax = plt.subplots(figsize=(10,8))
fig.suptitle('Temperature Sensor', fontsize='x-large')
ax.autoscale()
ax.grid()
#ax.xaxis.set_visible(False)
ax.tick_params(axis='x',labelcolor='w')
ax.set_ylabel('° Celcius')
ax.set_xlabel('Time')
legend_trigger = mpatches.Patch(color='green', label='Trigger Threshold')
legend_temp = mpatches.Patch(color='blue', label='Temperature')
fig.canvas.draw()

while a <= 60:
    temp = sensor.get_temperature(W1ThermSensor.DEGREES_C)
    temp_list.append(temp)

    print(temp)

    x.append(a)
    a = a + 1
    sleep(0.5)
    
    if temp > trigger_threshold:
        ax.plot(x, temp_list, color='red')
        legend_temp = mpatches.Patch(color='red', label='Temperature')
        red.on()
    else:
        ax.plot(x, temp_list, color='blue')
        legend_temp = mpatches.Patch(color='blue', label='Temperature')
        red.off()

    markerline, stemlines, baseline = plt.stem(
        temp_list, linefmt='None', markerfmt='None', basefmt='C2-', bottom=trigger_threshold, use_line_collection=True)

    plt.legend(handles=[legend_temp, legend_trigger], bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    fig.canvas.draw()
