import os
import re

f_d = []
f_q = []
with open("document.txt","r") as sent_list:
    f_d.append(sent_list.read())
with open("query.txt","r") as query_list:
    f_q.append(query_list.read())

print(f_d_l = [str(f_d).lower()])#忽略大小写
f_q_l = [str(f_q).lower()]

f_d_l_s = [str(f_d_l).split("." or  "!" or "?")] # 将查询的文献进行分割
f_q_l_s = [str(f_q_l).split(" ") ]# 将查询的单词进行分割

line_num = 1 #记录文献的行数
word_num = 1 #记录查询的单词数量
#先查询单词出现的行号，再提取出每一行。
new_list = [] #将单词出现的行组成新的列表

for word_num in range(1,len(f_q_l_s)):
    for line_num in range(1,len(f_d_l_s)):
        if f_q_l_s[word_num] in f_d_l_s[line_num]:
            new_list.append(f_d_l_s[line_num])
            line_num += 1
            word_num += 1
        else:
            print("None")

for word_num in range(len(new_list)):
    pos = 1  # 记录单词在句子中的具体位置
    if f_q_l_s[word_num] in new_list:
        pos = new_list.index(f_q_l_s[word_num])
        new_list[pos] = '$'
        pos += 1

print("{}/{}".format(line_num,pos))




