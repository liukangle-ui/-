#! /usr/bin/env python
#-*- coding: utf-8 -*-
#coding:gbk
"""
第一个小项目:Rock-paper-scissors-lizard-Spock
作者：刘康乐
日期：2020/11/22
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
# 以下为完成游戏所需要用到的自定义函数

"""
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Error-name_to_number")

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Error-number_to_name")
def rpsls(player_choice):
    print("===============================")
    print("你的选择为：",player_choice)
    play_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("计算机的选择为：",comp_choice)

    n = (play_number - comp_number) % 5

    if n==1 or n==2:
        print("你赢了!")
    elif n==3 or n==4:
        print("机器赢了!")
    elif n==0:
        print("相同")
    else:
        print("Error: No Correct Name")
"""
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()#输入玩家要出的方式
def name_to_number(name):#定义一个从名字转化为数的函数
    if name == "石头":
        return 0
    elif name == "史波克":
        return 1
    elif name == "纸":
        return 2
    elif name == "蜥蜴":
        return 3
    elif choice_name == "剪刀":
        return 4
    else:

       print("Error-name_to_number")

def number_to_name(number):#定义一个数字到名字的函数
    if number == 0:
        return "石头"
    elif number == 1:
        return "史波克"
    elif number == 2:
        return "纸"
    elif number == 3:
        return "蜥蜴"
    elif number == 4:
        return "剪刀"
    else:
        print("Error-number_to_name")
def rpsls(choice_name):#定义一个rpsls函数，用来对机器和玩家所出结果比较
    play_number = name_to_number(choice_name)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("计算机的选择为：",comp_choice)

    n = (play_number - comp_number) % 5

    if n==1 or n==2:#利用if函数进行比较
        print("你赢了!")
    elif n==3 or n==4:
        print("机器赢了!")
    elif n==0:
        print("相同")
    else:
        print("Error: No Correct Name")
rpsls(choice_name)
