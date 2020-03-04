import os
import re

f_d = []
f_q = []
with open("document.txt","r") as sent_list:
    f_d.append(sent_list.read())
with open("query.txt","r") as query_list:
    f_q.append(query_list.read())

def literature_query():

    f_d_s = f_d.split("." or  "!" or "?") # 将查询的文献进行分割
    f_q_s = f_q.split(" ")  # 将查询的单词进行分割

    f_d_s_l = f_d_s.lower() #忽略大小写
    f_q_s_l = f_q_s.lower()

    if f_q_s_l in f_d_s_l:

        line_num = f_d_s_l.index(f_q_s_l)
        word = f_d_s_l[cind].split("")
        word_num = word.index(f_q_s_l)

    print("{}/{}".format(line_num,word_num))



literature_query()

