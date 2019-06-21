import matplotlib.pyplot as plt
import numpy as np
import math


def separate(x):
    return x[::2] + x[1::2]


def fast_fourier_transform(f):
    n = len(f)
    if n >= 2:
        s = separate(f)
        first_half = fast_fourier_transform(s[:n/2])
        second_half = fast_fourier_transform(s[n/2:])
        s = first_half + second_half
        for i in range(n/2):
            e = s[i]
            o = s[n/2+i]
            w = np.exp((0-2j)*np.pi*i)
            s[i] = e+o*w
            s[n/2+i] = e - o*w
        return s
    else:
        return f


def start_fourier_transform():
    print "insert sample's size: "
    size = int(input())
    print "insert frequencies: "
    done = 'n'
    frequencies = []
    while done == 'n':
        frequencies.append(float(input()))
        print "Are you done? n/y"
        done = raw_input()
    signal = [sum(map(lambda f: math.sin(2*np.pi*t/size*f), frequencies))
              for t in range(size)]
    f = fast_fourier_transform(signal)
    print "FFT"
    for i in range(size):
        print ("{0:3.2f}".format(np.abs(f[i])))
    n_sample = []
    for i in range(size):
        n_sample.append(i)
    markerline, stemlines, baseline = plt.stem(n_sample, f, '-')
    plt.setp(baseline, color='black', linewidth=2)
    plt.setp(stemlines, color='black', linewidth=1)

    plt.show()


def signal_plotting():
    print "1 - Exponential sample \n" \
          "2 - Sqrt root sample \n" \
          "3 - Cos(x) sample \n" \
          "4 - Sin(x) sample \n" \
          "5 - Other sample \n"
    option = int(input())
    n_sample = []
    xn = []
    print "insert sample size: "
    size = int(input())
    if option == 1:
        print "insert values of n: "
        for i in range(size):
            sample = float(input())
            n_sample.append(sample)
        print "value to elevate: "
        value = int(input())
        xn = np.power(n_sample, value)

    if option == 2:
        print "insert values of n: "
        for i in range(size):
            sample = float(input())
            n_sample.append(sample)
        xn = np.sqrt(n_sample)

    if option == 3:
        print "insert values of n: "
        for i in range(size):
            sample = float(input())
            n_sample.append(sample)
        xn = np.cos(n_sample)

    if option == 4:
        print "insert values of n: "
        for i in range(size):
            sample = float(input())
            n_sample.append(sample)
        xn = np.sin(n_sample)

    if option == 5:
        for i in range(size):
            print "insert value of n: "
            sample = float(input())
            n_sample.append(sample)
            print "insert value of x[n]: "
            y = float(input())
            xn.append(y)

    markerline, stemlines, baseline = plt.stem(n_sample, xn, '-')
    plt.setp(baseline, color='black', linewidth=2)
    plt.setp(stemlines, color='black', linewidth=1)

    plt.show()


def discreet_signal_convolution():
    print "insert first sample size: "
    size1 = int(input())
    sample_1 = []
    for i in range(size1):
        print "x[", i, "]: "
        xn = float(input())
        sample_1.append(xn)
    print "insert second sample size: "
    size2 = int(input())
    sample_2 = []
    for i in range(size1):
        print "x[", i, "]: "
        xn = float(input())
        sample_2.append(xn)
    size = size1+size2-1
    conv_vector = []
    print "[Calculating convolution through Discreet Convolution's formula SUM(from j=0 to k = 2*n-1){f(j)*g(k-j)}]"
    for i in range(size):
        sum_elements = 0
        for k in range(i+1):
            try:
                sum_elements += sample_1[i-k]*sample_2[k]
                print "Multiplication of first signal sample Y_1 * second signal sample Y_2: ", sample_1[i - k], "*", \
                    sample_2[k], "\n"
            except:
                sum_elements += 0
        print "[Appending sample signal: ", sum_elements, " to new sample signal vector] \n"
        conv_vector.append(sum_elements)
    print "[End of convolution]\n" \
          "[Returning and printing result on the screen]"

    return conv_vector


print "1 - Signal plotting \n" \
      "2 - Convolution of two signals \n" \
      "3 - Fourier Transform"
op = int(input())
if op == 1:
    signal_plotting()
if op == 2:
    result_signal = discreet_signal_convolution()
    print "Result: "
    for i in range(len(result_signal)):
        print "YR[", i, "]: ", result_signal[i]
if op == 3:
    start_fourier_transform()
