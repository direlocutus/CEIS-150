# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 01:40:47 2021

@author: gardn
"""

count =0
sum =0
name = input("What is your Full name: ")
min_price = float(input("What is your minimmum price today: $"))
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 
79.3, 101.2]
for i in price_list:  
    if i>min_price:
        count = count+1
        sum = i + sum
print("Hello",name,"your minimmum price today is $",min_price)
print("There are ",count,"prices that are greater than your minimmum price.")
print("The total price is $",sum)