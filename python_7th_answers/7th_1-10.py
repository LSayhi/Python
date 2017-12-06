# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:01:36 2017

@author: LSayhi
"""

#homework for python 7_1 ~ 7-10
#7-1
'''
car=input('What kind of car do you want to rent? ')
print('Let me see if i can find you a '+car)
'''
#7-2
'''
number=input('How many people are watting for your foods? ')
number=int(number)
if number>8:
    print('sorry,there is no empty table.')
else:
    print('weclome,there are some tables.')
'''
#7-3
'''
number=input('please input a number: ')
number=int(number)
if number%10 == 0:
    print(str(number)+' is '+str(int(number/10))+' times of 10.')
else:
    print(str(number)+' is not any integer multiples of 10.')
'''
#7-4
'''
print("please input foods you wish, input 'quit' to exit if you want")
foods=[]
active=1
while active:
    food=input()
    if food != 'quit':
        print(food+' has been added. ')
        foods.append(str(food))
    else:
        active=0
print('The foods you wish is/are: ')
for food in foods:
    print(food,end=',')
'''
#7-5
'''
age=1
while age:
    age=int(input('please input your age(1-200 years,0 to quit):'))
    if age <3 and age >0:
        print('free to wantch')
    elif age>=3 and age<=12:
        print('you need pay 10 dollars')
    elif age>12:
        print('you need pay 15 dollars')
'''
#7-6
'''
print("please input foods you wish, input 'quit' to exit if you want")
foods=[]
while True:
    food=input()
    if food != 'quit':
        print(food+' has been added. ')
        foods.append(str(food))
    else:
        break
print('The foods you wish is/are: ')
for food in foods:
    print(food,end=',')
'''
#7-7
'''
while True:
    print('busy')
'''
#7-8
'''
swh='sanwich'
sanwich_orders=['tomato-'+swh,'meat-'+swh,'cheese-'+swh]
finished_sandwiches=[]
while sanwich_orders:
    sanwich_temp=sanwich_orders.pop()
    print('I made you '+sanwich_temp)
    finished_sandwiches.append(sanwich_temp)
print('sanwiches list:')
for sanwich in finished_sandwiches:
    print(sanwich)
'''
#7-9
'''
swh='sanwich'
sanwich_orders=['tomato-'+swh,'meat-'+swh,'pastrami'+swh,'cheese-'+swh,
                'pastrami'+swh,'mayo'+swh,'pastrami'+swh]
while ('pastrami'+swh) in sanwich_orders:
    sanwich_orders.remove('pastrami'+swh)
print(sanwich_orders)
'''
#7-10
'''
name_place={}
active=True
while active:
    name =input("What's your name:")
    place=input('where do you want to viste:')
    name_place[name]=place
    flag=input('Is there anyone others want to join?(y/n): ')
    #if flag != 'y' or 'yes':
    if flag !=('y' or 'yes'):
        active=False
for name,place in name_place.items():
    print(name.title()+' want to viste '+place)
'''