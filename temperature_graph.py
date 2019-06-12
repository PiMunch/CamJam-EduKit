# needs w1thermsensor [sudo apt install python3-w1thermsensor]

import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

temp_list = []
x = []
a = 0
temp = 0

#SET-UP GRAPH
plt.ion()
fig, ax = plt.subplots(figsize=(10,8))
fig.suptitle('Temperature Sensor', fontsize='x-large')
ax.autoscale()
ax.grid()
ax.set_ylabel('Temperature\n(°C)')
ax.set_xlabel('Time')
fig.canvas.draw()

while True:
    temp = sensor.get_temperature(W1ThermSensor.DEGREES_C)
    temp_list.append(temp)

    print(temp)

    x.append(a)
    a = a + 1
    sleep(0.5)
    
    if temp > 28:
        ax.plot(x, temp_list, color='red')
    else:
        ax.plot(x, temp_list, color='blue')

    fig.canvas.draw()
