import numpy as np

q=20
l=5

x = np.linspace(0,l,20)

M = q/2*(l*x-x**2)
V = q*(1/2-x)

print("Moment")
print(M)
print("Moment")
print(V)