#!/usr/bin/env python
# -*- coding:utf-8 -*-
#if-else
sex = input("input your gender:")
if sex == "girl":
    print("I would like to have a little monkey with A!")
    print("the second line!")
elif sex == "man":
    print("Going to homosexual!...")
else:
    print("Pervert!")

#猜lucky number,n=6
#猜的数字 比6大，提示说你打印小一点
#猜的数字 比6小，提示说你打印大一点
#猜的数字 ==6，bingo
#while
luckyNumber = 6
guessCounter = 0
while  guessCounter<3:
    inputNumber = int(input("Input the guess num:"))
    if inputNumber> luckyNumber:
        print("the real number is smaller.")
    elif inputNumber< luckyNumber:
        print("the real number is bigger.")
    else:
        print("Bingo!")
        break
    guessCounter+=1
else:
    print("Too many tries...")

#猜lucky number,n=6
#猜的数字 比6大，提示说你打印小一点
#猜的数字 比6小，提示说你打印大一点
#猜的数字 ==6，bingo
#for
luckyNumber = 6
for i in range(3):
    inputNumber = int(input("Input the guess num:"))
    if inputNumber > luckyNumber:
        print("the real number is smaller.")
    elif inputNumber < luckyNumber:
        print("the real number is bigger.")
    else:
        print("Bingo!")
        break
else:
    print("Too many tries...")