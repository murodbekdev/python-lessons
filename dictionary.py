# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:08:38 2023

@author: Murodjon
"""

# Dictrinary in Python 


car_0 = {'model':'mustang', 'color':'black'}

print(car_0['model'])
print(car_0['color'])

en_uz = {'apple':'olma', 'apricot':'o\'rik', 'pear':'nok', 'banana':'banan'}



mevalar = {'olma':10000, 'tarvuz':8000, 'qovun':10000}
print(f"Olma narhi {mevalar['olma']} so'm")


talaba_0 = {'ism':'murdojon gafforov','yosh':28, 't_yil':1995}

print(f"{talaba_0['ism'].title()},{talaba_0['t_yil']} -yilda tug'ilgan, {talaba_0['yosh']} yoshda") # lug'atning ichiga qo'shimcha kalitlar qo'shishimiz mumkin msalan 

talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatika'  # bo'sh lug;at bilan ham to'ldirishimiz mumkin 

talaba_1 = {}

talaba_1['ism'] = 'gafforov murodjon'
talaba_1['fakultet'] = 'Artificial Intelligence'
talaba_1['kurs'] = 1
talaba_1['yosh'] = 28

print(f"{talaba_1['ism'].title()}, {talaba_1['fakultet']}ning {talaba_1['kurs']}- kursda ta'lim oladi', {talaba_1['yosh']} da")

# endi o'chirib tashlashni ko'radigan bo'lsak 

# del operatri orqali o'chirib tashlaymiz 

del talaba_1['kurs']
print(talaba_1)



# endi esa biz lug'atda yo'q narsalarni bilish uchun get methodidan foydalansak bo'ladi

meva = en_uz.get('pineapple', 'Bu mevani hayotini kayb etting')
print(meva)   # agar get() methodidagi keydan keyin value bermasakngiz consoleda None chiqadi

