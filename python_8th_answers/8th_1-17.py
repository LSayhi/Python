# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:58:46 2017

@author: LSayhi
"""
#homework for python 8th lecture
#8-1
'''
def display_msg():
    print(' You will learn "function" in this lecture ')
display_msg()
'''
#8-2
'''
def favorite_book(title):
    print('One of my favorite book is '+title.title())
favorite_book('《Python编程从入门到实践》' )
'''
#8-3
'''
def make_shirt(size,word):
    print('Size is '+size+', word is '+"'"+word+"'")
make_shirt('L','we are BYR')
make_shirt(word='Best',size='XXL')
'''
#8-4
'''
def make_shirt(size='Large',word='I love python'):
    print('Size is '+size+', word is '+"'"+word+"'")
make_shirt()
make_shirt('middle')
make_shirt('XL','we are JUFE')
'''
#8-5
'''
def describe_city(city,country='Iceland'):
    print(city+' is in '+country)
describe_city('Reykjavik')
describe_city(city='Beijing',country='China')
describe_city('Tokyo','Japan')
'''
#8-6
'''
def describe_city(city,country):
    message='"'+city+', '+country+'"'
    return message
msg=describe_city('Reykjavik','Iceland')
print(msg)
msg=describe_city(city='Beijing',country='China')
print(msg)
msg=describe_city('Tokyo','Japan')
print(msg)
'''
#8-7
'''
def make_album(name,album,songsnum=''):
    name_album={}
    name_album['name'] =name
    name_album['album']=album
    if songsnum:
        name_album['songnum']=songsnum
    return name_album
print(make_album('周杰伦','范特西'))
print(make_album('周杰伦','七里香','10'))
print(make_album('周杰伦','哎呦不错呦','12'))
'''
#8-8
'''
def make_album(name='',album='',songsnum=''): 
    name_album={}
    if name:
        name_album['name'] =name
    if album:
        name_album['album']=album
    if songsnum:
        name_album['songnum']=songsnum
    return name_album
while True:
    name=input("please input star's name: ")
    if (name=='quit'):
        break
    ablum=input("ablum name: ")
    if (ablum=='quit'):
        break
    songsnum=input("the ablum song numbers: ")
    if (songsnum=='quit'):
        break
    print(make_album(name,ablum,songsnum))
'''
#8-9
'''
def show_magicans(magcianlist):
    for magican in magcianlist:
        print(magican)
magicans=['Divad','Liuqian','JackMa']
show_magicans(magicans)
'''
#8-10
'''
def make_great(magicanlist):
    for i in range(len(magicanlist)):
        magicanlist[i]='the Great '+magicanlist[i]
def show_magicans(pmagicanlist):
    for pmagican in pmagicanlist:
        print(pmagican)
magicans=['Divad','Liuqian','JackMa']
make_great(magicans)
show_magicans(magicans)
'''
#8-11
'''
def make_great(magicanlist):
    for i in range(len(magicanlist)):
        magicanlist[i]='the Great '+magicanlist[i]
    return magicanlist
def show_magicans(pmagicanlist):
    for pmagican in pmagicanlist:
        print(pmagican)
magicans=['Divad','Liuqian','JackMa']
magicanss=make_great(magicans[:])
show_magicans(magicans)
show_magicans(magicanss)
'''
#8-12
'''
def make_sandwich(*gredients):
    print(gredients)
make_sandwich('mushroom')
make_sandwich('mushiroom','cheese')
make_sandwich('mushiroom','cheese','peppers')
'''
#8-13
'''
def build_profile(first,last,**user_info):
    profile={}
    profile['fisrt_name']=first
    profile['last_name'] =last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('jiangfan','liu',age='17',
                           location='beijing',field='EE')
print(user_profile)
'''
#8-14
'''
def make_car(manufacturer,version,**car_info):
    carinfo={}
    carinfo['manufacturer']=manufacturer
    carinfo['version'] =version
    for key,value in car_info.items():
        carinfo[key]=value
    return carinfo
car_profile=make_car('BMW','3',color='blue',
                           maxspeed='350km/h')
print(car_profile)
'''
#8-15
'''
from printing_function import print_models  as pm
from printing_function import show_completed_models as scm
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
pm(unprinted_designs,completed_models)
scm(completed_models)
'''
#8-16
'''
import print_helloworld
print_helloworld.helloworld()
'''
'''
from print_helloworld import helloworld
helloworld()
'''
'''
from print_helloworld import helloworld as hw
hw()
'''
'''
import print_helloworld as phw
phw.helloworld()
'''
'''
from print_helloworld import *
helloworld()
'''
#8-17
'''see as above'''