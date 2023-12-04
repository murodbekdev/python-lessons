# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:48:14 2023

@author: Murodjon
"""



dastruchilar = {
    'ali': ['ptyhon','django'],
    'rano': ['java', 'spring boot']
    }

for ism, tillar in dastruchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tili va frameworkini biladi:")
    for til in tillar:
        print(f'{til.upper()} ', end='')