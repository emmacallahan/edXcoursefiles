#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:01:13 2019

@author: ecallahan
"""
##Assume s is a string of lower case characters.

##Write a program that counts up the number of vowels contained in the string s. 
##Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
##For example, if s = 'azcbobobegghakl', your program should print:

##Number of vowels: 5
from how_many_vowels_in_string import s_string

def test_should_return_number_of_vowels_for_given_string_s():
    s_string = 'azcbobobegghakl'
    number_of_vowels = 5
    assert number_of_vowels == 5 