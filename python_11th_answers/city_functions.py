# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:08:06 2017

@author: LSayhi
"""

def city_of_country(city,country):
    """返回城市和国家的字符串"""
    string=city.title()+','+country.title()
    return string

def city_of_country_population(city,country,population):
    """返回城市、国家、人口的字符串"""
    string=city.title()+','+country.title()+'- '+'population '+population
    return string

def city_of_country_option(city,country,population=''):
    """返回城市、国家（人口可选）的字符串"""
    string=city.title()+','+country.title()+'- '+'population '+population
    return string