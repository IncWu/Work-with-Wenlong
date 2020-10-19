from PIL import Image
import os
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
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('D:/Python/software_engineering/Game/Question/Question_Image/'+str(index) + '.png', 'PNG')
        index += 1

def run():
    file_path = "D:/Python/software_engineering/GAME/Question/Full_Image.png"
    image = Image.open(file_path)
    #image.show()
    image_list = cut_image(image)
    save_images(image_list)
run()