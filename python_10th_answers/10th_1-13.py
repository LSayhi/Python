# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:15:44 2017

@author: LSayhi
"""
#homework for python 10th
#10-1
'''
file_name='learning_python.txt'
with open(file_name) as lp:
    contents=lp.read()
    print(contents.rstrip())
with open(file_name) as lp:
    for line in lp:
        print(line.rstrip())
with open(file_name) as lp:
    lines=lp.readlines()
for line in lines:
    print(line.strip())
'''
#10-2
'''
file_name='learning_python.txt'
with open(file_name) as lp:
    for line in lp:
        print(line.replace('python','C++').rstrip())
'''
#10-3
'''
class Guest_input():
    """访客类"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
guest_name=input('please input your name: ')
guest_age =input('please input your age : ')
guest=Guest_input(guest_name,guest_age)
with open('guest.txt','w') as file_obj:
    file_obj.write(guest.name+'\n')
    file_obj.write(guest.age+'\n')
with open('guest.txt','r') as file_obj:
    fo=file_obj.read()
    print(fo)
'''
#10-4
'''
class Guest_input():
    """访客类"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
guest_name=''
guest_name=''
while True:
    guest_name=str(input("please input your name('quit' to break): "))
    if guest_name=='quit':
        break
    guest_age =str(input("please input your age ('quit' to break): "))
    if guest_name=='quit':
        break
    guest=Guest_input(guest_name,guest_age)
    with open('guest.txt','a') as file_obj:
        file_obj.write(guest.name+' ')
        file_obj.write(guest.age+'\n')
with open('guest.txt','r') as file_obj:
     fo=file_obj.read()
     print(fo)
'''
#10-5
'''
while True:
    reason=str(input("Why you love programing?(q to quit):"))
    if reason =='q':
        break
    with open('reasons.txt','a') as file_obj:
        file_obj.write(reason)
with open('reasons.txt') as rea:
    print(rea.read())
'''
#10-6
'''
def two_sum(numa,numb):
    """两个数的和"""
    try:
        print(int(numa)+int(numb))
    except:
        print("What you input are not two numbers！")
a=input('plese input a number:')
b=input('plese input anther number:')
two_sum(a,b)
'''
#10-7
'''
def two_sum(numa,numb):
    """两个数的和"""
    try:
        c=int(numa)+int(numb)
    except:
        pass
    else:
        print(c)
while True:
    a=input('plese input a number(q to qiut):')
    b=input('plese input anther number(q to quit):')
    if(a=='q')or(b=='q'):
        break
    two_sum(a,b)
'''
#10-8
'''
try :
    with open('cats.txt') as cats_obj:
        cats=cats_obj.read()
    with open('dogs.txt') as dogs_obj:
        dogs=dogs_obj.read()
except:
    print('file not found')
else:
    print(cats)
    print(dogs)
'''
#10-9
'''
try :
    with open('cats.txt') as cats_obj:
        cats=cats_obj.read()
    with open('dogs.txt') as dogs_obj:
        dogs=dogs_obj.read()
except:
    pass
else:
    print(cats)
    print(dogs)
'''
#10-10
'''
try:
    with open('words_count.txt') as file_obj:
        lines=file_obj.readlines()
except:
    print('file not found')
else:
    a=0
    for line in lines:
        a+=line.lower().count('the')
    print(a)
'''
#10-11
'''
import json
filename='favorite_number.json'
favorite_num=input('please input your favorite number: ')
with open(filename,'w') as file_obj:
    json.dump(favorite_num,file_obj)
with open(filename,'r') as f_obj:
    f_n=json.load(f_obj)
    print("I know your favorite number! It's "+f_n)
'''
#10-12
'''
import json
def get_stored_number():
    """返回最喜欢的数字"""
    filename='lovenumber.json'
    try:
        with open(filename) as f_obj:
            favorite_number=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number
def new_favorite_number():
    """提示并存储最喜欢的数字"""
    favorite_number=input("What's your favorite number?: ")
    filename='lovenumber.json'
    with open(filename,'w') as f_obj:
        json.dump(favorite_number,f_obj)
    return favorite_number
def show_number():
    """显示最喜欢的数字"""
    favorite_number=get_stored_number()
    if favorite_number:
        print("I know your favorite number! It's "+favorite_number)
    else:
        favorite_number=new_favorite_number()
show_number()
'''
#10-13
'''
import json
def get_stored_username():
    """如果用户名存在，则获取用户名"""
    filename='username.json'
    try:
        with open(filename) as f_obj:
            user_name=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return user_name
def get_new_username():
    """提示输入用户名并存储返回"""
    user_name=input("so,what's your name?: ")
    filename='username.json'
    with open(filename,'w') as f_obj:
        json.dump(user_name,f_obj)
    return user_name
def greet_user():
    """询问用户名，并提示"""
    user_name=get_stored_username()
    label=input('Welcome,is that '+"'"+user_name+"'"+' your name?(y/n):')
    if label=='y':
        print("Wecome back "+user_name)
    else:
        user_name=get_new_username()
        print("well,I will remrember you when you come back")
greet_user()
'''
