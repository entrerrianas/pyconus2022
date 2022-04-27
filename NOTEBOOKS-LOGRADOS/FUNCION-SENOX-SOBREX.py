import matplotlib.pyplot as grafico
import numpy as np

X = np.linspace(-2 * np.pi, 2 * np.pi, 1001)
print(X)

Y = np.sin(X)/X
print(Y)

grafico.grid(True)
grafico.plot(X, Y, 'ro')
#[<matplotlib.lines.Line2D object at 0x000002B86F37DDC0>]

grafico.show()
