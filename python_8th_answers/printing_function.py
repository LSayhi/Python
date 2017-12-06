# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:06:34 2017

@author: BD
"""

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print('printing model: '+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
