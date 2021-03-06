# -*- coding:utf-8 -*-
import sys
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import random
import math
import time
import image_compare




def run():
    global zero_location
    global way
    global swap
    swap = []
    way = str()
    mc = run_Axing()
    #step存储每一步变化完的九宫格
    global step
    step = []
    if mc > -1:
        zero_location = []
        num = 0
        step = [openList[mc]]
        new_list = []
        while mc > 0:
            mc = before[mc]
            step.append(openList[mc])
            num += 1
        #print('次数：', num)
        for i in range(0, num + 1):
            #print('step', i)
            b = 0
            list1 = []

            for j in range(0, 3):
                list1 = list1 + (step[num - i][j * 3:j * 3 + 3])
                #print(step[num - i][j * 3:j * 3 + 3])

            #print("list1", list1)
            b = get_zero_location(list1)
            zero_location.append(b)
        way = get_zero_path(zero_location)

    else:
        print('ERROR!')
    #print(way)
    #print('finsh')
    return way,swap
def get_zero_path(list):
    global zero_path
    zero_path = str()
    index = 0
    while index < len(list)-1:
        if list[index] - list[index+1] == 3:
            zero_path+=str('w')
        elif list[index] - list[index+1] == 1:
            zero_path+=str('a')
        elif list[index] - list[index + 1] == -3:
            zero_path+= str('s')
        elif list[index] - list[index + 1] == -1:
            zero_path+=str('d')
        index += 1
    return zero_path
def get_zero_location(list):
    a = 0
    for i in list:
        if i == 0:
            a = list.index(i)+1
            print(a)
    return a

def turn(x,y,li):
    #1-9
    #交换位置，返回数组和空格的位置
    temp = li[:]
    temp[x-1] = li[y-1]
    temp[y-1] = li[x-1]
    return temp

def bool_rules(first,next):
    """判断移动是否合法1-9"""
    if (first>9)|(first<1)|(next>9)|(next<1):
        return 0
    elif (first%3==0)&(next%3==1):
        return 0
    elif (first%3==1)&(next%3==0):
        return 0
    elif ((abs(first-next)==3)|(abs(first-next)==1)):
        return 1
    else:
        return 0

def cmp(q,p):#不同为1 ，相同为0
    if len(q)-len(p)!=0:
        return 1
    x=0
    for i in range(0,len(q)):
        if q[i]!=p[i]:
            return 1
    return 0

def H_cost(li1,li2):#当前搜索点到目标点的估计代价
    pay=0
    for i in range(0,len(li1)):
        pay+=abs(li1[i]-li2[i])
    return pay
def run_Axing():
    global swap
    global move
    global before
    global cost
    global openList
    global closeList
    before = [0]
    cost = [0]
    openList = [[]]
    closeList = []
    blank = image_compare.bk
    li_goal = list(range(1, 9 + 1))
    #    entry_num=int(entry_num)

    li_goal[blank - 1] = 0
    # li0 = image_compare.array
    #print(li_goal)
    li0 = image_compare.array

    #print('li0', li0)
    swap = []
    move = [-3, 3, -1, 1]
    maxcount=10000+81
    # 1. 把起始格添加到开启列表。
    openList[0]=li0[:]
    #print('openlist[0]', openList[0])
    cost[0]=H_cost(li_goal,openList[0])
    #print('cost[0]',cost[0])
    before[0]=0
    Gn = 0
 #   add_open(st[0])
    # 2.重复如下的工作：
    while len(closeList)<10000:
        # a) 寻找开启列表中H值最低的格子。我们称它为当前格。
        mc = cost.index(min(cost))
        if cmp(openList[mc][:],li_goal[:])==0:
            return mc
        x = openList[mc].index(0) + 1
        # b) 把它切换到关闭列表。
        closeList.append(openList[mc][:])
        cost[mc]=maxcount
#        del openList[mc]
#        del cost[mc]
        # c) 对相邻的4格中的每一个进行以下操作

        for i in range(0, 4):
            if bool_rules(x, x + move[i]):
                temp = turn(x, x + move[i], openList[mc][:])[:]
                if closeList.count([temp]) == 0:  # 如果它不可通过或者已经在关闭列表中，略过它。
                    if openList.count([temp]) == 0:
                        openList.append(temp)  # 如果它不在开启列表中，把它添加进去。把当前格作为这一格的父节点。记录这一格的H值。
                        c = H_cost(li_goal, openList[-1])+Gn
                        cost.append(c)
                        before.append(mc)
                        # 如果它已经在开启列表中，用H值为参考检查新的路径是否更好。
                        # 更低的H值意味着更好的路径。如果是这样，就把这一格的父节点改成当前格，
                        # 并且重新计算这一格的H值。
                    else:
                        t = openList.index(temp)
                        c = H_cost(li_goal, openList[t])+Gn
                        if c < cost[t]:
                            cost[t]=c
                            before[t] = mc
        Gn += 1
    #print(before)
    return -1



zero_way,answer_swap= run()
