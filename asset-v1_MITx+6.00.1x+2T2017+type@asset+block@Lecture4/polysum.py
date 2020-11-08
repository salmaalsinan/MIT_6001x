#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 22:12:09 2019

"""
# import numpy library 
# alternativly you can import math
import numpy as np 

def polysum(n,s):

    ''' 
    
    inputs:
        number of sides of polygon (n:int) 
        length of side (s:float)
        
    Returns:
        sum of the area and square of 
        the perimeter of the polygon
        rounded to 4 decimal places

    '''
 
    if n ==0: # incase someone accidently put 0 
        
        print ('Please enter a correct value for n')
           
    else:
        
        area = (.25*n*(s**2))/(np.tan(3.14/n))
        perimeter = s*n
        
        Sum=area+(perimeter**2) 
   
        return round(Sum,4) # round to fourth decimel


