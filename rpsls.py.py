#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

#import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��
import random
#coding:gbk
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
    print("����������ѡ��",player_choice)
    play_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("�������ѡ��Ϊ��",comp_choice)

    n = (play_number - comp_number) % 5

    if n==1 or n==2:
        print("��Ӯ��!")
    elif n==3 or n==4:
        print("����Ӯ��!")
    elif n==0:
        print("��ͬ")
    else:
        print("Error: No Correct Name")
"""
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
def name_to_number(name):
    if name == "ʯͷ":
        return 0
    elif name == "ʷ����":
        return 1
    elif name == "��":
        return 2
    elif name == "����":
        return 3
    elif choice_name == "����":
        return 4
    else:

       print("Error-name_to_number")

def number_to_name(number):
    if number == 0:
        return "ʯͷ"
    elif number == 1:
        return "ʷ����"
    elif number == 2:
        return "��"
    elif number == 3:
        return "����"
    elif number == 4:
        return "����"
    else:
        print("Error-number_to_name")
def rpsls(choice_name):
    play_number = name_to_number(choice_name)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print("�������ѡ��Ϊ��",comp_choice)

    n = (play_number - comp_number) % 5

    if n==1 or n==2:
        print("��Ӯ��!")
    elif n==3 or n==4:
        print("����Ӯ��!")
    elif n==0:
        print("��ͬ")
    else:
        print("Error: No Correct Name")
rpsls(choice_name)
