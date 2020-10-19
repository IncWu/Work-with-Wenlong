#! /usr/local/bin/python3

# -*- coding: utf-8 -*-
import os

from PIL import Image
def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0,3):#两重循环，生成9张图片基于原图的位置
        for j in range(0,3):
            #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    return image_list

#保存
def save_images(image_list,num):
    index = 1
    os.mkdir('D:/Python/software_engineering/Game/img/' + str(num))
    for image in image_list:
        image.save('D:/Python/software_engineering/Game/img/'+str(num)+'/'+str(index) + '.png', 'PNG')
        index += 1

if __name__ == '__main__':
    i=1
    file_path = "D:/Python/software_engineering/无框字符/无框字符/"
    for pic in os.listdir(file_path):
        image = Image.open(file_path+pic)
        #image.show()
        image_list = cut_image(image)
        save_images(image_list,i)
        i+=1