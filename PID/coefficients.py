#!/usr/bin/env python3
from numpy import array, dot, transpose
import numpy as np
from numpy.linalg import inv
import time
import math


tp = 0.3
T = 6.3

R = 7.6922075
k = 0.48
J = 0.0024376
Jt = 6.2*10**(-4)
Jk = 9.715*10**(-6)
Mt = 0.4412
Mk = 0.024411
l = 0.11
r = 0.02817042493
g = 9.8


X1 = Mt*l*r*(Mt*l*r - 2*J) - (Mt*l**2 + Jt)*(Mt*r**2 + 2*Mk*r**2 + 2*Jk + 2*J)

A = array([[0, 0, 1],
     	   [Mt**2*g*l**2*r/X1, 2*(k**2)*(Mt*l*r + Mt*l**2 + Jt)/(R*X1), 0],
     	   [-Mt*g*l*(Mt*r**2 + 2*Mk*r**2 + 2*Jk + 2*J)/X1, -2*(k**2)*(Mt*l*r + Mt*r**2 + 2*Mk*r**2 + 2*Jk)/(R*X1), 0]])

B = array([[0],
           [-2*k*(Mt*l*r + Mt*l**2 + Jt)/R/X1],
           [2*k*(Mt*l*r + Mt*r**2 + 2*Mk*r**2 + 2*Jk)/R/X1]])

print(A)
print(B)

C = array( [ [ 0, 										B[1,0], 								B[2,0] ],
             [ B[2,0], 									0, 										A[2,1] * B[1,0] - A[1,1] * B[2,0] ],
             [ A[2,1] * B[1,0] - A[1,1] * B[2,0],	 	A[1,0] * B[2,0] - A[2,0] * B[1,0], 		0 ] ] )

C = inv(C)


for tp in range(10,60,1):

    tp = tp * 0.01

    W = T / tp



    D = array( [ [ 3*W + A[1,1] ],
                 [ 3*W**2 + A[2,0] ],
                 [ W**3 - A[1,1]*A[2,0] + A[1,0]*A[2,1] ] ])



    K = dot(C, D)
    K = K.transpose()
    print(tp, list(K[0]*math.pi/180))
