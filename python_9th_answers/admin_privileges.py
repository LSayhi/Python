# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:25:02 2017

@author: BD
"""
"""特权类和管理员类"""
from user_only import User
class Privilege():
    """特权类"""
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        print('following are privileges admins have: ')
        for privilege in self.privileges:
            print(privilege.strip())
class Admin(User):
    """管理员类，继承user类"""
    def __init__(self,first_name,last_name,**user_info):
        super().__init__(first_name,last_name,**user_info)
        self.privileges=Privilege()