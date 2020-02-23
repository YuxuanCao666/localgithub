import re

formula = input()

Operators = ['+', '-', '*', '/', '^', '(', ')']




def mul_div(list,x):
    list = re.findall('[\d\.]+|\+|\-|\*|\/|\^|\(|\)', formula)
    a = list.index(x)
    print(a)
    if x == '*':
        k = float(list[a-1]) * float(list[a+1])
    elif x == '/':
        k = float(list[a-1]) / float(list[a+1])
    del list[a - 1]
    del list[a - 1]
    del list[a - 1]  # 删除掉列表里刚做运算的三个元素
    list.insert(a - 1, str(k))  # 将刚计算的结果插入到列表中然后执行下一次计算
    return list
print(list)
print(a)