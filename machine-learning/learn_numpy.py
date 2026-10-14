import numpy as np

number = np.random.randn(20)

A = np.random.rand(3,2)
B = np.random.rand(2,3)

print(number)
print(number[number >= 0])

matrice = number.reshape(4,5)
print(matrice)