import base64
import os
from PIL import Image
import numpy as np
import Cut_Question_Image

#Cut_Question_Image.run()
FileList=os.listdir('D:/Python/software_engineering/Game/img/')
#寻找与问题图片匹配的图片文件
def find_image():
    for dir in FileList:
        count = 0
        fileName=[]
        picList=os.listdir('D:/Python/software_engineering/Game/img/'+dir)
        for p in os.listdir('D:/Python/software_engineering/Game/Question/Question_Image/'):
            for pic in picList:
                with open('D:/Python/software_engineering/Game/Question/Question_Image/'+p, 'rb') as f1:
                    base64_problem = base64.b64encode(f1.read())
                with open('D:/Python/software_engineering/Game/img/'+dir+'/'+pic,'rb') as f:
                    base64_data=base64.b64encode(f.read())
                if base64_data==base64_problem:
                    count=count+1
        if count==8:
            return dir
def make_block(m):
    sign=[1,2,3,4,5,6,7,8,9]
    blanknumber=[1,2,3,4,5,6,7,8,9]
    temp=[]
    block=np.arange(1,10).reshape(3,3)
    for pic2 in os.listdir('D:/Python/software_engineering/Game/Question/Question_Image/'):
        for pic1 in os.listdir('D:/Python/software_engineering/Game/img/' +m):
            with open ('D:/Python/software_engineering/Game/img/'+m+'/'+pic1,'rb') as f1:
                base64_f1=base64.b64encode(f1.read())
            with open ('D:/Python/software_engineering/Game/Question/Question_Image/'+pic2,'rb') as f2:
                base64_f2=base64.b64encode(f2.read())
            if base64_f1==base64_f2:
                number=int(pic2.split('.')[0])
                col=(number-1)%3
                row=int((number-1)/3)
                block[row][col]=pic1.split('.')[0]
                temp.append(int(pic1.split('.')[0]))
                sign.remove(number)
                blanknumber.remove(int(pic1.split('.')[0]))
    block[int((sign[0]-1)/3)][(sign[0]-1)%3]=blanknumber[0]
    return temp,block,sign[0],blanknumber[0]
def judgment(temp):
    signal=0
    position=-1
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            if temp[i]>temp[j]:
                signal+=1
            if signal==1:
                position=i
    if signal%2!=0:
        print('no way')
        return signal,position
def swap(block,p):

    if p==0:  #交换的第一个数为第一格
        if block[(p+1)//3][(p+1)%3]==bk:#如果下一格为挖去的格子
            tempnumber=block[p//3][p%3]
            block[p//3][p%3]=block[(p+2)//3][(p+2)%3]
            block[(p + 2) // 3][(p + 2) % 3]=tempnumber
            print('swap[%d , %d]' % (p, p + 2))
            return p,p+2
        else:
            tempnumber = block[p // 3][p % 3]
            block[p // 3][p % 3] = block[(p + 1) // 3][(p + 1) % 3]
            block[(p + 1) // 3][(p + 1) % 3] = tempnumber
            print('swap[%d , %d]' % (p, p + 1))
            return p,p+1
    else:
        if block[(p+1)//3][(p+1)%3]==bk:#如果下一格为挖去的格子
            tempnumber = block[p // 3][p % 3]
            block[p // 3][p % 3] = block[(p + 2) // 3][(p + 2) % 3]
            block[(p + 2) // 3][(p + 2) % 3] = tempnumber
            print('swap[%d , %d]' % (p, p + 2))
            return p,p+2
        elif p>=blank:#空格在交换的位置之前
            tempnumber = block[(p + 1) // 3][(p + 1) % 3]
            block[(p + 1) // 3][(p + 1) % 3] = block[(p + 2) // 3][(p + 2) % 3]
            block[(p + 2) // 3][(p + 2) % 3] = tempnumber
            print('swap[%d , %d]' % (p + 1, p + 2))
            return p+1,p+2
        else:
            tempnumber = block[p // 3][p % 3]
            block[p // 3][p % 3] = block[(p + 1) // 3][(p + 1) % 3]
            block[(p + 1) // 3][(p + 1) % 3] = tempnumber
            print('swap[%d , %d]' % (p, p + 1))
            return p,p+1
def turnToarray(block,bk):
    t=[]
    for i in range(3):
        for j in range(3):
            if block[i][j]!=bk:
                t.append(block[i][j])
            else:
                t.append(0)
    return t
def turnToarray_1(block):
    t=[]
    for i in range(3):
        for j in range(3):
                t.append(block[i][j])
    return t
m=find_image()
numberarray,board,blank,bk=make_block(m)
array=turnToarray(board,bk)
#print('numberarray',numberarray)
#print('bk',bk)
#print('array',array)
#print(turnToarray_1(board))
#print('blank',blank)
#print('m',m)