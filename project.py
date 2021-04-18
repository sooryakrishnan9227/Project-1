# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 00:25:39 2021

@author: rajas
"""

rad=float(input("enter the radius:"))
import math
print("The area of the circle with radius "+str(rad)+"is:"+str(math.pi*rad*rad))

filename= input("Enter File Name:")
f=filename.split(".")
print("The extension of the file is :" + f[-1])
