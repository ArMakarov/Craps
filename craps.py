# -*- coding: utf-8 -*-
"""Craps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ack6YDVihG_7HJq_RjIoRIE9s_LN58T
"""

import random 
lst = [1,2,3,4,5,6]
a = random.choice(lst)
b = random.choice(lst)
c = a+b
goal = 0
if c in [7,11]:
  print('You won!');
if c in [2,3,12]:
  print('You lose!');
if c in [4, 5, 6, 8, 9 , 10]:
  c_1 = 0
  stop = 0
  goal = c
  while stop !=1:
    a_1 = random.choice(lst)
    b_1 = random.choice(lst)
    c_1 = a_1 + b_1
    if c_1 == goal:
      stop = 1
      print('You won!');
    if c_1 == 7:
      stop =1 
      print('You lose!')

