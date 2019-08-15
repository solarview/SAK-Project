from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import time
import sak_gpio

fig = plt.figure()
ax = plt.axes(xlim=(1, 8), ylim=(0, 200))
line, = ax.plot([], [], lw=2)
plt.ylabel('bpm')
plt.title('bpm')

bpm_history = [0, 0, 0, 0, 0, 0, 0, 0]

def init():
    global line
    line.set_data([], [])
    return line,

def animate(i):
    global bpm_history, line
    bpm_history.append(getbpm())

    if len(bpm_history) >= 8:
        del bpm_history[0]
    
    xar = [i for i in range(1, 9)]

    line.set_data(np.array(xar), np.array(bpm_history))
    return line,


def getbpm() -> int:
    return sak_gpio.get_bpm()

def start_gui():
    global fig
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=200, blit=True)
    plt.show()


start_gui()