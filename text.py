# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:37:18 2021

@author: אביב
"""
# C:\python\mt2\text.txt


def revword(word:str) -> str:
    the_word = word 
    the_lower_word = the_word.lower()
    str1 = the_lower_word[::-1]
    print(str1)
    return (str1)

def countword()->int:
    file = input("please enter the file path: ")
    text_file = open(file , "r")
    text_file = text_file.read()
    text_file = text_file.lower()
    text_list = text_file.split()
    count =0
    first_word = text_list[0]
    text_list = text_list[1:]
    
    for word in range(len(text_list)):
        str2=revword(text_list[word])
        if (first_word == str2 ):
            count = count+1
    print(count+1)
    return(count+1)

countword()