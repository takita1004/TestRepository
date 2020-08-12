import numpy as np
import matplotlib.pyplot as plt

A = np.zeros((9000,9000),dtype=np.float64)
    
for i in range(9000):
    for k in range(9000):
        c=complex(-2.0+i/3000,-1.5+k/3000)
        z=0j
        for h in range (100):
            z=z*z+c
            if (z.real*z.real+z.imag*z.imag)>=4:
                A[k,i]=h        
                break

#plt.gca().set_aspect('equal', adjustable='box')
plt.figure(figsize=(5,5),dpi=354)
plt.contourf(A,100,cmap='Blues_r')
#plt.savefig("manndelblot3.jpg")
