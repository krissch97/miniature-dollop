import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return 1 - 1 * np.exp(-t/10)
def g(t):
    return 1 * np.exp(-(t-100)/10)
def h(t):
    return 1 - 1 * np.exp(-(t-200)/10)
def i(t):
    return 1 * np.exp(-(t-300)/10)
    
def j(t):
    return t * 0 + 1
def k(t):
    return t * 0

t1 = np.arange(0.0, 101.0, 1.0)
t2 = np.arange(100.0, 201.0, 1.0)
t3 = np.arange(200.0, 301.0, 1.0)
t4 = np.arange(300.0, 401.0, 1.0)
#t2 = np.arange(25.0, 226.0, 1.0)

plt.plot([0, 100, 101, 200, 201, 300, 301, 400], [1, 1, 0, 0, 1, 1, 0, 0])
plt.plot( t1, f(t1), t2, g(t2), t3, h(t3), t4, i(t4), color='orange')

#plt.plot(t1, j(t1), t2, k(t2), t3, j(t3), t4, k(t4))
#for i in range(1, 6):
#    plt.plot(i, f(i), marker="o")

#plt.xlabel('τ')
#plt.xlabel('Time [ms]')
plt.xlabel('Time [μm]')
plt.ylabel('Voltage [V]')
plt.show()