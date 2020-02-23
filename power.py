import re

formula = input ()

Operators = ['+','-','*','/','^','(',')']

list = re.findall('[\d\.]+|\+|\-|\*|\/|\^|\(|\)',formula )
def power(list,sign):
    a = list.index(sign)
    if x == '^':
        b = str(float(list[a - 1])**float(list[a + 1]))
    else :
        return list
    del list[a - 1]
    del list[a - 1]
    del list[a - 1]
    list.insert(a - 1, b)
    return list
print(list)
