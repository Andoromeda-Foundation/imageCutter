# -*-coding:utf8 -*- 
import Image
import os

# L 928 px, W 621 px
#start, 57, 57
count=0
filename = '1.1.jpg'
im = Image.open(filename)
fn = os.path.basename(filename)


for py in range(57,57+3*928,928):
    for px in range(57,57+3*621,621):
        qx=px+621
        qy=py+928
        count=count+1
        back=fn+str(count)+'.jpg'
        im.crop((px,py,qx,qy)).save(back)


py = 57+3*928
for px in range(57,57+2*928,928):
    qx=px+928
    qy=py+621
    count=count+1
    back=fn+str(count)+'.jpg'
    im.crop((px,py,qx,qy)).rotate(270).save(back)



