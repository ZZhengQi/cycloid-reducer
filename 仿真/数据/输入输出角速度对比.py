import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from pylab import *

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  
'''
x = np.linspace(0, 10, num=601)
y = genfromtxt('偏置轴套-2.csv',delimiter= '，')
y2 = np.ones(601)*480
'''

u = 1
n = 140 * np.pi / 180
x = np.linspace(0,4*np.pi,num=256)

y = u * np.cos(n)*10/(1 - pow(np.sin(n),2) * pow(np.sin(x),2))
y2 = u * np.cos(n)*10/(1 - pow(np.sin(n),2) * pow(np.cos(x),2))

'''
y = pow(np.sin(x),2)
y2 = pow(np.sin(x ),2)
'''

plt.figure(figsize=(12,8))

font2 = {
'size'   : 18,
}

'''
#plt.plot(x,y)
plt.subplot(2,1,1)
plt.plot(x,y2,color='red')
plt.xlabel('转动角度（rad）',font2)
plt.ylabel('角速度（rad/s）',font2)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.subplot(2,1,2)
plt.plot(x,y)
#plt.plot(x,y2)
plt.xlabel('转动角度（rad）',font2)
plt.ylabel('角速度（rad/s）',font2)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.show()
'''
plt.plot(x,y)
plt.xlabel('转动角度（rad）',font2)
plt.ylabel('角速度（rad/s）',font2)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.plot(x,y2,color='red')

plt.show()