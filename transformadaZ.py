# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

def plotarCirculoUnitario():
    t = np.arange(0, 2*np.pi, 0.01)
    x = np.cos(t)
    y = np.sin(t)
    plt.plot(x, y)
    plt.grid()

# Os polos são os pontos verdes
def plotarPolos(polos):
    for i in range(len(polos)):
        plt.plot(polos[i].imag, polos[i].real, 'o', color='green')

# Os zeros são os pontos vermelhos
def plotarZeros(zeros):
    for i in range(len(zeros)):
        plt.plot(zeros[i].imag, zeros[i].real, 'o', color='red')

def plotarPolosZeros(polos, zeros):
    plotarCirculoUnitario()
    plotarPolos(polos)
    plotarZeros(zeros)
    plt.axis("equal")
    plt.show()

def calcularPolosZeros(num, den):
    polos = np.roots(num)
    zeros = np.roots(den)
    plotarPolosZeros(polos, zeros)

def capturarCoef(n):
    vetor = []
    for i in range(n):
        coef = float(input())
        vetor.append(coef)
    return vetor


# Inicio da main
num = []
print("Digite a quantidade de coeficientes do numerador:")
n = int(input())
print("Digite os coeficientes do numerador:")
num = capturarCoef(n)

den = []
print("Digite a quantidade de coeficientes do denomidador:")
n = int(input())
print("Digite os coeficientes do denominador:")
den = capturarCoef(n)

calcularPolosZeros(num, den)