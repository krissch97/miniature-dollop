import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return 1 - 1 * np.exp(-t/10)
def g(t):
    return (f(16.7)) * np.exp(-(t-16.7)/10)
def h(t):
    return 1 + (g(33.3)- 1) * np.exp(-(t-33.3)/10)
def i(t):
    return (h(50)) * np.exp(-(t-50)/10)
    
def j(t):
    return t * 0 + 1
def k(t):
    return t * 0

t1 = np.arange(0.0, 16.8, 0.1)
t2 = np.arange(16.7, 33.4, 0.1)
t3 = np.arange(33.3, 50.1, 0.1)
t4 = np.arange(50.0, 66.8, 0.1)
#t2 = np.arange(25.0, 226.0, 1.0)

plt.plot([0, 16.8, 16.7, 33.4, 33.3, 50.0, 50.1, 66.7], [1, 1, 0, 0, 1, 1, 0, 0])
plt.plot( t1, f(t1), t2, g(t2), t3, h(t3), t4, i(t4), color='orange')

#plt.plot(t1, j(t1), t2, k(t2), t3, j(t3), t4, k(t4))
#for i in range(1, 6):
#    plt.plot(i, f(i), marker="o")

#plt.xlabel('τ')
#plt.xlabel('Time [ms]')
plt.xlabel('Time [μm]')
plt.ylabel('Voltage [V]')
plt.show()
