# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:48:14 2023

@author: Murodjon
"""


talaba_0 = {
    'ism': 'murodjon',
    'familiya':'gafforov',
    'yosh':28,
    'jins':'erkak',
    'fakultetl':'artficial intelligence',
    'kurs':1
    }

# Biz hozirda dictionarydagi bazi method'laarni ko'rib chiqamiz.

print(talaba_0.items())

for key, value in talaba_0.items():
    print(f"Kalit: {key}")
    print(f"Qiymati: {value}\n")  #yani items() orqali har bitta lug;atning key va value'lariga kirib chiqayapmiz
    
    
    
    
telefonlar = {
    'ali':'galaxy x',
    'vali':'iphone 14 pro',
    'hasan':'huawei 10 pro',
    'husan':'samsung note 10'
    }

for key, value in telefonlar.items():
    print(f"{key.title()}ning telefoni {value}\n")
    
    
    
# keys() methodi bilan ham foydalanamiz, bu asosan kalitlarni chiqadi yani

maxsulotlar = {
    'olma':10000,
    'nok':8000,
    'uzum':25000
    
    }


print(maxsulotlar.keys())
# buni endi for sikli bilan chiqarsak 

print("Do'kondagi maxsulotlar:")
for maxsulot in maxsulotlar.keys():
    print(maxsulot.title())
    
    
    
# keling sal foydali dastur tuzamiz

bozorlik = ['anor', 'olma','uzum','gosht']
for maxsulot in maxsulotlar:
    if maxsulot in bozorlik:
        print(f"{maxsulot.title()} {maxsulotlar[maxsulot]} so'm")
        
for buyum in bozorlik:
    if buyum not in maxsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
        
        
# sorted() ham bor bunda kalit so'z bo'yicha tahlab beradi 

for maxsulot in sorted(maxsulotlar):
    print(maxsulot.title())
        
    
# endi esa biz asosan qiymatlarni ham chiqarishimiz mumkin masalan 

print("Maxsulotlar narxi:")

for maxsulot in maxsulotlar:
    print(maxsulot)
        
print("Users mostly used those types of telephones:")
for tel in set(telefonlar.values()):
    print(tel)