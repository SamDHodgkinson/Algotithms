# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:05:47 2017

@author: Samuel
"""
import numpy as np
import math
import matplotlib.pyplot as plt


data = np.loadtxt('data.txt')

x = data[:,0]
y = data[:,1]
e = data[:,2]

p=q=r=s=t=0

for xi, yi, ei in zip(x,y,e):
    p += 1/(ei**2)
    q += xi/(ei**2)
    r += yi/(ei**2)
    s += xi**2/(ei**2)
    t += xi*yi/(ei**2)

delta = p*s - q**2

a = (r*s - q*t)/delta
b = (p*t - q*r)/delta
    
ua = math.sqrt(s/delta)
ub = math.sqrt(p/delta)

print("a =", a ,"ua =", ua)
print("b =", b ,"ub =" ,ub)

yb = a + b*x

txt = 'y = (',format(a,'.3f'),' +/- ',format(ua,'.3f'),')'' + (',format(b,'.3f'),'x',' +/- ',format(ub,'.3f'),')'
txt2 = ''.join(map(str,txt))
                  
plt.xlabel("x")
plt.ylabel("y")
plt.errorbar(x,y,e,fmt='o')
plt.title("Graph of y against x")
plt.plot(x,yb)
plt.figtext(0.35,0.15,txt2)
