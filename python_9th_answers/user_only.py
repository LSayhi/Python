# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:23:22 2017

@author: LSayhi
"""
"""单独的User类，useronly"""
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