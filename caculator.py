#_*_coding:utf-8_*_
__author__ = 'cyx'
import re

formula = input ()

Operators = ['+','-','*','/','^','(',')']
list = re.findall('[\d\.]+|\+|\-|\*|\/|\^|\(|\)', formula)

#判断格式
for j in range(len(formula)):
    if formula[j] in Operators and formula[j+1] in Operators:
        print('FORMAT ERROR')
    elif formula[j].isalpha():
        print('INPUT ERROR')
    elif formula[j] == '/' and formula[j+1] == '0':
        print('VALUE ERROR')

#乘方计算
def power(list,sign):
    a = list.index(sign)
    if sign == '^':
        b = str(float(list[a - 1])**float(list[a + 1]))
    else :
        return list
    del list[a]
    del list[a - 1]
    del list[a + 1]
    list.insert(a - 1, b)
    return list

#*、/计算
def mul_div(list,sign):
    a = list.index(sign)
    if sign == '*':
        c = float(list[a-1]) * float(list[a+1])
    elif sign == '/':
        c = float(list[a-1]) / float(list[a+1])
    # 删除掉列表里刚做运算的三个元素，并将刚计算的结果插入到列表中然后执行下一次计算
    del list[a]
    del list[a - 1]
    del list[a +1]
    list.insert(a - 1, str(c))
    return list

#+、-、*、/、^综合
def fun(list):
    sum = 0
    while 1:
        if '^' in list and '*' not in list and '/' not in list:
            power(list,'^')
        elif '^' not in list and '*' in list and '/' not in list:
            mul_div(list, '*')
        elif '^' not in list and '*' not in list and '/' in list:
            mul_div(list, '/')
        elif '^' in list and '*' in list and '/' in list:
            a = list.index('*')
            b = list.index('/')

            if a < b:
                power(list,'^') + mul_div(list, '*')
            elif a > b:
                power(list,'^') + mul_div(list, '/')
        else :
            for l in range(1, i , 2):
                if list[l] == '+' and list[l] == '-':
                    sum -= float(list[l + 2])
                elif list[l] == '+' and list[l + 1] != '-':
                    sum += float(list[l + 1])
                elif list[l] == '-' and list[l + 1] == '-':
                    sum += float(list[l + 2])
                elif list[l] == '-' and list[l + 1] != '-':
                    sum -= float(list[l + 1])
        break
    return sum


#检测括号，计算括号内的值，再替代回去。
def calculator(formula):
    l_bracket = []
    bracket_ans = 0
    if '(' not in formula:
        bracket_ans = fun(formula)
        return bracket_ans
    for k in range(i):
        if formula[k] =='(':
            l_bracket = k
        if formula[k] == ')':
            r_bracket = k
            a = 0  # 定义一个变量 存储括号表达式的结果
            eq = expression[l_bracket:r_bracket]  # 获取括号里的表达式
            a = fun(eq)  # 调用该函数计算括号里的表达式的值
            formula = formula[0:l_bracket[len(l_bracket) - 1]] + str(a) + formula[i + 1:len(formula) + 1]
        return calculator(formula)

print(calculator(formula))




