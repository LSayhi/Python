# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:05:55 2017

@author: LSayhi
"""
#homework for python 5-8，……，5-11
#5-8
'''
user_names=['bu','yao','shuo','admin','shi','tian','cai']
for user in user_names:
    if user =='admin':
        print('hello admin,would you like to see a status report?')
    else:
        print('hello'+user+',thank you for logging in again.')
'''
#5-9
'''
user_names=['bu','yao','shuo','admin','shi','tian','cai']
if user_names:
    for user in user_names:
        if user =='admin':
            print('hello admin,would you like to see a status report?')
        else:
            print('hello'+user+',thank you for logging in again.')
else:
    print('We need to find some users.')
user_names=[]
if not user_names:
    print('we need to find some usres.')
'''
#5-10
'''
current_users=['bu','yao','shuo','wo','shi','tian','cai','HI']
i=0
for current_user in current_users:
    current_users[i]=current_user.lower()
    i=i+1
new_users=['Bu','bili','shuo','hi','helloworld']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("'"+new_user+"'"+" is already exist,please input other's name")
    else:
        print("'"+new_user+"'"+' can be used.')
'''
#5-11
numbers=[1,2,3,4,5,6]
for number in numbers:
    if number == 1:
        print(str(number)+'st')
    elif number == 2:
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')
