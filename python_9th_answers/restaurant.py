# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 22:09:32 2017

@author: LSayhi
"""
"""一个可用于表示餐馆的类"""
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
