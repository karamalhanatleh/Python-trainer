# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:01:23 2022

@author: KRM0201517
"""

import pandas as pd
import numpy as np

'''
myarray = np.array([[6,9,8,5,4,2],
                    [0,2,5,6,3,9],
                    [8,5,4,1,2,3],
                    [6,9,8,5,4,2],
                    [0,5,3,6,9,8],
                    [8,7,4,5,2,3]])

rownames = ['a', 'b','c','d','e','f']
colnames = ['one', 'two', 'three','four','five','six']

df = pd.DataFrame(myarray, index=rownames, columns=colnames)
print(df)

'''


'''
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades)
print(grades['Math'])

print('Math' in grades.keys())
print('math' in grades.keys())
print(12 in grades.values)
print(55 in grades.values)

'''


w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.stack())





















