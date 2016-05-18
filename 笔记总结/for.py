#!/usr/bin/env python
# -*- coding:utf-8 -*-
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