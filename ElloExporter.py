# -*- coding: utf-8 -*-
import json
import codecs

filePath = raw_input("输入你的.json文件名（含后缀）：")
if filePath == "":
    filePath ='twisted_meadows_export.json'

f1 = open(filePath,'r')
data = json.load(f1)

f = codecs.open("output.txt",'w',"utf-8")


#读取json结构里的post部分，筛选出内容输出至文件
for i in data['posts']:

    f.write(i["created_at"])
    f.write("\n")
    for j in i["body"]:
        if j["kind"] == "text":
            f.write(j["data"])
            f.write("\n")
        elif j["kind"] == "image" or j["kind"] == "embed":
            f.write(j["data"]["url"])
            f.write("\n")
        else:
            #我的post里面只有三种类型，所以不知道其他类型的结构如何
            #如果强行采用一样的方式读取，会报错，所以对未知类型跳过
            #如有需要，可以根据报错信息自行添加判断语句
            print "Error!"
            print "can't recognize this item : ",j["kind"]
            print "The type of this item is ",type(j)
        f.write("\n")

    f.write("==========================\n\n")

f1.close()
f.close()

print "Complete!"
print "所有post已保存在当前目录下的output.txt文件中"
