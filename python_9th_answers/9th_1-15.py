# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:57:24 2017

@author: LSayhi
"""
#homework for python 9th 1-15
#9-1
'''
class Restaurant():
     """餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+
              "\nThe restaurant's type is "+self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is now opening')
restaurant= Restaurant('鱼米之乡','川菜系')
restaurant.describe_restaurant()
restaurant.open_restaurant()
'''
#9-2
'''
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+
              "\nThe restaurant's type is "+self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is now opening')
restaurant1= Restaurant('鱼米之乡','川菜系')
restaurant1.describe_restaurant()
restaurant2= Restaurant('赣南食府','江浙系')
restaurant2.describe_restaurant()
restaurant3= Restaurant('心灵鸡排','fast food')
restaurant3.describe_restaurant()
'''
#9-3
'''
class User():
    def __init__(self,first_name,last_name,**user_info):
        self.first_name=first_name
        self.last_name =last_name
        self.user_info =user_info
    def descibe_user(self):
        print('The user is '+self.first_name+self.last_name)
        print('following are his/her information:')
        print(self.user_info)
    def greet_user(self):
        print('weclome,'+self.first_name+self.last_name)
user1=User('liu','jiangfan',age='21',location='Beijing')
user1.descibe_user()
user1.greet_user()
user2=User('jiang','zeming',age='92',location='Beijing')
user2.descibe_user()
user2.greet_user()
'''
#9-4
'''
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+
              "\nThe restaurant's type is "+self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is now opening')
    def set_number_served(self,latest_number):
        self.number_served=latest_number
    def increment_number_served(self,plus_number):
        self.number_served+=plus_number
restaurant= Restaurant('鱼米之乡','川菜系')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.set_number_served(200)
print(restaurant.number_served)
restaurant.increment_number_served(36)
print(restaurant.number_served)
'''
#9-5
'''
class User():
    def __init__(self,first_name,last_name,**user_info):
        self.first_name=first_name
        self.last_name =last_name
        self.user_info =user_info
        self.login_attempts=0
    def descibe_user(self):
        print('The user is '+self.first_name+self.last_name)
        print('following are his/her information:')
        print(self.user_info)
    def greet_user(self):
        print('weclome,'+self.first_name+self.last_name)
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
user1=User('liu','jiangfan',age='21',location='Beijing')
user1.descibe_user()
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
'''
#9-6
'''
class Restaurant():
    """餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("The restaurant's name is "+self.restaurant_name+
              "\nThe restaurant's type is "+self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is now opening')
class Icecreamstand(Restaurant):
    """冰淇凌店类，继承Restaurant类"""
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['a','b','c']
    def describe_icecreams(self):
        print('following are flavor types we have: ')
        for flavor in self.flavors:
            print(flavor.strip())
icecream=Icecreamstand('KFC','fast food')
icecream.describe_restaurant()
icecream.describe_icecreams()
'''
#9-7
'''
class User():
    """用户信息"""
    def __init__(self,first_name,last_name,**user_info):
        self.first_name=first_name
        self.last_name =last_name
        self.user_info =user_info
        self.login_attempts=0
    def descibe_user(self):
        print('The user is '+self.first_name+self.last_name)
        print('following are his/her information:')
        print(self.user_info)
    def greet_user(self):
        print('weclome,'+self.first_name+self.last_name)
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
class Admin(User):
    """管理员类，继承user类"""
    def __init__(self,first_name,last_name,**user_info):
        super().__init__(first_name,last_name,**user_info)
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        print('following are privileges admins have: ')
        for privilege in self.privileges:
            print(privilege.strip())
adminuser=Admin('Liu','Jiangfan',level='admin')
adminuser.descibe_user()
adminuser.show_privileges()
'''
#9-8
'''
class Privilege():
    """特权类"""
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        print('following are privileges admins have: ')
        for privilege in self.privileges:
            print(privilege.strip())
class User():
    """用户信息"""
    def __init__(self,first_name,last_name,**user_info):
        self.first_name=first_name
        self.last_name =last_name
        self.user_info =user_info
        self.login_attempts=0
    def descibe_user(self):
        print('The user is '+self.first_name+self.last_name)
        print('following are his/her information:')
        print(self.user_info)
    def greet_user(self):
        print('weclome,'+self.first_name+self.last_name)
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
class Admin(User):
    """管理员类，继承user类"""
    def __init__(self,first_name,last_name,**user_info):
        super().__init__(first_name,last_name,**user_info)
        self.privileges=Privilege()
adminuser=Admin('Liu','Jiangfan',level='admin')
adminuser.descibe_user()
adminuser.privileges.show_privileges()
'''
#9-9
'''
class Car():
    """"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_desciptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name
    def read_read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class Battery():
    """"""
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery")
    def get_range(self):
        if self.battery_size==70:
            ranges=240
        elif self.battery_size==85:
            ranges=270
        msg="This car can go approximately "+str(ranges)
        msg+=" miles on a full charge."
        print(msg)
    def upgrade_battery(self):
        if self.battery_size !=85:
            self.battery_size=85
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
my_tesla=ElectricCar('Tesla','model s',2016)
print(my_tesla.get_desciptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
'''
#9-10
'''
"""从restaurant.py中导入Restaurant类"""
from restaurant import Restaurant
restaurant= Restaurant('鱼米之乡','川菜系')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.set_number_served(200)
print(restaurant.number_served)
restaurant.increment_number_served(36)
print(restaurant.number_served)
'''
#9-11
'''
"""从user.py模块中导入三个类"""
from user import Privilege,User,Admin
adminuser=Admin('Liu','Jiangfan',level='admin')
adminuser.descibe_user()
adminuser.privileges.show_privileges()
'''
#9-12
'''
"""从两个模块中导入三个类"""
from user_only import User
from admin_privileges import Admin,Privilege
adminuser=Admin('Liu','Jiangfan',level='admin')
adminuser.descibe_user()
adminuser.privileges.show_privileges()
'''
#9-13
 