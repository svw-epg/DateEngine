# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:53:22 2020

@author: ZhuangWenjia
"""

#2+4+6+8+...+100
sum = 2
number = 2
while number < 51:
       sum += number*2
       number += 1
print(sum)

sum=0
for num in range(2,101,2):
    sum +=num
print(sum); 

import numpy as np
a=np.arange(2,101,2)
print(np.sum(a))

import numpy as np
a=np.arange(2,101,2)
sum=0
for num in a:
    sum +=num
print(sum);