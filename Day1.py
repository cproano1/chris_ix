#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:11:33 2018

@author: Chris
"""

#%%
# FizzBuzz
x = range(100)
list(x)
for n in x:
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
        
#%%
#Roman Numbers
numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def num_Roman(num):

    roman = ''

    while num > 0:
        for n, r in numbers:
            while num >= n:
                roman += r
                num -= n

    return roman

#%%
#Caesar Cipher
def caesar(txt, key):
    txt = txt.lower()
    cipher = ""
    for letter in txt:
        shifted = ord(letter) + key
        if shifted < 97:
            shifted += 26
        if shifted > 123:
            shifted -= 26
        cipher += chr(shifted)
    return cipher

print(caesar("abcd", 13))

        