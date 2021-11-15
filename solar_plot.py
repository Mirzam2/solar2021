import numpy as np
import matplotlib.pyplot as plt
list_v = np.array([])
list_r = np.array([])
list_t = np.array([])
def go_plot(list):
    for i in list:
        list_t = np.append(list_t,i[0])
        list_v = np.append(list_v,i[1])
        list_r = np.append(list_r,i[2])
    sp = plt.subplot(311)
    plt.plot()
    plt.title()
    plt.grid(True)

