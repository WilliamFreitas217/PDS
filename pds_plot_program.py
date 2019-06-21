import matplotlib.pyplot as plt
import numpy as np


def impulse(tam, negative=False, cte=1):
    pulse = []
    if negative:
        for i in range(int(tam)):
            pulse.append(cte*(-1.))
    else:
        for i in range(int(tam)):
            pulse.append(cte*(1.))
    return pulse


def cosseno(s_begin=0, s_end=4, s_passe=1):
    # TODO First plot
    t = np.arange(s_begin, s_end*np.pi, s_passe)
    x = np.cos(t)
    plt.plot(t, x)
    plt.show()

    # TODO Second plot
    pulse = impulse(s_end*np.pi)
    negative_pulse = impulse(s_end*np.pi, negative=True)
    plt.stem(t, pulse)
    plt.show()

    # TODO Third plot
    plt.plot(t, x)
    plt.stem(t, negative_pulse)
    plt.stem(t, pulse)
    plt.show()

    # TODO Fourth plot
    tm = s_end*np.pi/s_passe
    x = np.linspace(s_passe, s_end * np.pi, tm)
    y = np.cos(x)
    plt.stem(x, y)
    plt.show()


def seno(s_begin=0, s_end=4, s_passe=1):
    # TODO First plot
    t = np.arange(s_begin, s_end*np.pi, s_passe)
    x = np.sin(t)
    plt.plot(t, x)
    plt.show()

    # TODO Second plot
    pulse = impulse(s_end*np.pi)
    negative_pulse = impulse(s_end*np.pi, negative=True)
    plt.stem(t, pulse)
    plt.show()

    # TODO Third plot
    plt.plot(t, x)
    plt.stem(t, negative_pulse)
    plt.stem(t, pulse)
    plt.show()

    # TODO Fourth plot
    tm = s_end*np.pi/s_passe
    x = np.linspace(s_passe, s_end * np.pi, tm)
    y = np.sin(x)
    plt.stem(x, y)
    plt.show()


def kxsen(s_begin=0, s_end=4, s_passe=1, k=1):
    t = np.arange(s_begin, s_end * np.pi, s_passe)
    x = np.sin(t)
    plt.plot(t, k*x)
    plt.show()

    pulse = impulse(s_end * np.pi, cte=k)
    plt.stem(t, pulse)
    plt.show()

    plt.plot(t, k*x)
    negative_pulse = impulse(s_end * np.pi, negative=True, cte=k)
    plt.stem(t, negative_pulse)
    plt.stem(t, pulse)
    plt.show()

    tm = s_end*np.pi/s_passe
    x = np.linspace(s_passe, s_end * np.pi, tm)
    y = np.sin(x)
    plt.stem(x, k*y)
    plt.show()


def kxcos(s_begin=0, s_end=4, s_passe=1, k=1):
    t = np.arange(s_begin, s_end * np.pi, s_passe)
    x = np.cos(t)
    plt.plot(t, k*x)
    plt.show()

    pulse = impulse(s_end * np.pi, cte=k)
    plt.stem(t, pulse)
    plt.show()

    plt.plot(t, k*x)
    negative_pulse = impulse(s_end * np.pi, negative=True, cte=k)
    plt.stem(t, negative_pulse)
    plt.stem(t, pulse)
    plt.show()

    tm = s_end*np.pi/s_passe
    x = np.linspace(s_passe, s_end * np.pi, tm)
    y = np.cos(x)
    plt.stem(x, k*y)
    plt.show()


def cosplussin(s_begin=0, s_end=4, s_passe=1, k=1):
    t = np.arange(s_begin, s_end * np.pi, s_passe)
    x = np.cos(t) + np.sin(t)
    plt.plot(t, k*x)
    plt.show()

    pulse = impulse(s_end * np.pi, cte=k)
    plt.stem(t, pulse)
    plt.show()

    plt.plot(t, k*x)
    negative_pulse = impulse(s_end * np.pi, negative=True, cte=k)
    plt.stem(t, negative_pulse)
    plt.stem(t, pulse)
    plt.show()

    tm = s_end*np.pi/s_passe
    x = np.linspace(s_passe, s_end * np.pi, tm)
    y = np.cos(x) + np.sin(t)
    plt.stem(x, k*y)
    plt.show()


def cosxsin(s_begin=0, s_end=4, s_passe=1, k=1):
    t = np.arange(s_begin, s_end * np.pi, s_passe)
    x = np.cos(t) * np.sin(t)
    plt.plot(t, k*x)
    plt.show()

    pulse = impulse(s_end * np.pi, cte=k)
    plt.stem(t, pulse)
    plt.show()

    plt.plot(t, k*x)
    negative_pulse = impulse(s_end * np.pi, negative=True, cte=k)
    plt.stem(t, negative_pulse)
    plt.stem(t, pulse)
    plt.show()

    tm = s_end*np.pi/s_passe
    x = np.linspace(s_passe, s_end * np.pi, tm)
    y = np.cos(x) * np.sin(t)
    plt.stem(x, k*y)
    plt.show()


op = raw_input("Option: ")
beginning = int(input("Signal's beginning: "))
end = int(input("Signal's end: "))
passe = int(input("Signal's passe: "))

if '1' in op:
    cosseno(beginning, end, passe)
if '2' in op:
    seno(beginning, end, passe)
if '3' in op:
    k = int(input("Cte to be multiplied: "))
    kxsen(beginning, end, passe, k)
if '4' in op:
    k = int(input("Cte to be multiplied: "))
    kxcos(beginning, end, passe, k)
if '5' in op:
    cosplussin(beginning, end, passe)
