# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 22:43:10 2017

@author: LSayhi
"""

#homework 5-2 in python
#1
print('1th :\nplease input two strings:\n')
name1=input()
name2=input()
print('if they are the same?\n')
if name1==name2:
    print('\tthey are equal!\n')
else:
    print('\tthey are not equal\n')
print('if they are the same after lower?\n')
if name1.lower()==name2.lower():
    print('\tthey are equal!\n')
else:
    print('\tthey are not equal\n')
#2
print('2th :\nplease input a string:\n')
list=['apple','red','bule']
string=input()
if string in list:
    print('The input string is in the very list\n')
else:
    print('The string is not in the very list\n')