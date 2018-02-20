# -*-coding:utf8 -*- 
import Image
import os

# L 925 px, W 616px
#start, 566, 59
count=0
filename = '1.2.jpg'
im = Image.open(filename)
fn = os.path.basename(filename)


for py in range(59,59+3*925,925):
    for px in range(566,566+3*616,616):
        qx=px+616
        qy=py+925
        count=count+1
        back=fn+str(count)+'.jpg'
        im.crop((px,py,qx,qy)).save(back)


py = 59+3*928
for px in range(566,566+2*925,925):
    qx=px+925
    qy=py+616
    count=count+1
    back=fn+str(count)+'.jpg'
    im.crop((px,py,qx,qy)).rotate(90).save(back)



