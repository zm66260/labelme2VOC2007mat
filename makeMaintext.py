
import os
import random

trainval_percent = 0.8
train_percent = 0.8
xmlfilepath = '../WIDER_Face_MAFA/Annotations'
txtsavepath = '../WIDER_Face_MAFA/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open('../WIDER_Face_MAFA/ImageSets/Main/trainval.txt', 'w')
ftest = open('../WIDER_Face_MAFA/ImageSets/Main/test.txt', 'w')
ftrain = open('../WIDER_Face_MAFA/ImageSets/Main/train.txt', 'w')
fval = open('../WIDER_Face_MAFA/ImageSets/Main/val.txt', 'w')

for i in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
