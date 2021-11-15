import numpy as np
import matplotlib.pyplot as plt
list_v = np.array([])
list_r = np.array([])
list_t = np.array([])
def go_plot(list):
    global list_v
    global list_r
    global list_t
    for i in list:
        list_t = np.append(list_t,i[0])
        list_v = np.append(list_v,i[1])
        list_r = np.append(list_r,i[2])
    sp = plt.subplot(311)
    plt.plot(list_t, list_v)
    plt.title("Зависимость v от t")
    plt.grid(True)
    sp = plt.subplot(312)
    plt.plot(list_t, list_r)
    plt.title("Зависимость r от t")
    plt.grid(True)
    sp = plt.subplot(313)
    plt.plot(list_v, list_r)
    plt.title("Зависимость v от r")
    plt.grid(True)
    plt.show()
