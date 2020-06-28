# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:32:45 2020

@author: Morgann
"""
## Write a Python program to convert an integer to a roman numera

def entier_to_romain(nombre):
    chiffres_romain = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    romain = ''
    while nombre > 0:
        for i, r in chiffres_romain:
            while nombre >= i:   ## On  va se balader dans le tableau des milliers centaines, dizaines ... etc pour constituer le chiffre romain
                romain = romain + r
                nombre = nombre - i
    return romain