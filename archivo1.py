import numpy as np
import pylab as pl
# Crea un vector (arreglo) con los valores del ehe X
x = [5000,6000,7000,8000,9000]
# Crea un vector (arreglo) con valores en el eje Y para cada valor en el eje X
y = [65,78,88,89,93]
# Grafica el vector x contra el vector y
pl.plot(x, y)# Crea un vector (arreglo) con valores en el eje Y para cada valor en el eje X
x1 = [7000,8000,9000,10000,11000]
# Crea un vector (arreglo) con valores en el eje Y para cada valor en el eje X
y2 = [65,75,85,86,90]
# Grafica el vector x contra el vector y
pl.plot(x1, y2)
pl.xlabel('Voltaje [V]')
pl.ylabel('Eficiencia [%]')
# Guarda el grafico en formato png
pl.savefig('temp1.png')


