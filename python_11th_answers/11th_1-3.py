# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:48:33 2017

@author: LSayhi
"""
#homework for python 11th
#11-1 test_cities.py
'''
from city_functions import city_of_country
import unittest
class CityCountryTest(unittest.TestCase):
    """"测试city_functions.py"""
    def test_city_country(self):
        string=city_of_country('Santiago','Chile')
        self.assertEqual(string,'Santiago,Chile')
unittest.main()
'''
#11-2
'''
from city_functions import city_of_country
from city_functions import city_of_country_option
from city_functions import city_of_country_population
import unittest
class CityCountryTest(unittest.TestCase):
    """"测试city_functions_*.py"""
    def test_city_country(self):
        string=city_of_country('Santiago','Chile')
        self.assertEqual(string,'Santiago,Chile')
    def test_city_country_population(self):
        string=city_of_country_population('Santiago','Chile','10000')
        self.assertEqual(string,'Santiago,Chile- population 10000')
    def test_city_country_option(self):
        stringa=city_of_country_option('Santiago','Chile','10000')
        self.assertEqual(stringa,'Santiago,Chile- population 10000')
        stringb=city_of_country('Santiago','Chile')
        self.assertEqual(stringb,'Santiago,Chile')
unittest.main()
'''
#11-3
'''
from employee import Employee
import unittest
class TestEmployee(unittest.TestCase):
    """测试Employee类"""
    def setUp(self):
        self.employeetest=Employee('Liu','jiangfan',1111)
    def test_give_default_rasie(self):
        self.assertEqual(self.employeetest.give_raise(),6111)
    def test_give_custom_rasie(self):
        self.assertEqual(self.employeetest.give_raise(8888),9999)
unittest.main()
'''