# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 17:36:02 2022

@author: KRM0201517
"""

import pandas as pd
data=['peter' , 'Paul' , 'MARY' , '15' , ' ']

print(pd.Series(data).str.len()) #length
print(pd.Series(data).str.startswith('p'))
print(pd.Series(data).str.endswith('Y'))



"""
c='karam soui ojpj s odij and iaji ali  '
c=c.split()
print(c)
print('\n\n\n')
print(len(c))
print(pd.Series(c).str.find('a'))
"""

print(pd.Series(data).str.find('t'))

print(pd.Series(data).str.rfind('t'))




print(pd.Series(data).str.rjust(20))
print(pd.Series(data).str.ljust(20))

print(pd.Series(data).str.isupper())
print(pd.Series(data).str.islower())
print(pd.Series(data).str.istitle())

print(pd.Series(data).str.isspace())
print(pd.Series(data).str.isdigit())
print(pd.Series(data).str.isalpha())
print('\n')


print(pd.Series(data).str.isalnum())
print(pd.Series(data).str.isnumeric())



print(pd.Series(data).str.upper())
print(pd.Series(data).str.capitalize())
















