#!usr/bin/env python
# -*- coding:utf-8 -*-

def logon():
    '''作业1：写登录器。要求输入用户名和密码,登录成功至欢迎词；三次登录失败，账户锁定且不能再次登录。'''
    for i in range(3):
        logonUserId = input("用户名：")
        logonPW = input("密码：")
        if logonUserId == "test" and logonPW == "pw":
            print("登录验证成功！\n %s  欢迎登录系统" %(logonUserId))
            break
        else:
            print("登录验证失败！%s次登录失败后账户将锁定！" %(2-i))
            if i>=2:
                print("3次登录失败！账户锁定！")

#logon()

def level3Menu():
    '''作业2：三级菜单。'''
    pass

level3Menu()
