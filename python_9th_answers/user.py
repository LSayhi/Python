# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:18:26 2017

@author: BD
"""
"""定义用户类，管理员类，特权类"""
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