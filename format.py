import re

formula = input ()
i = len(formula)

Operators = ['+','-','*','/','^','(',')']

list = re.findall('[\d\.]+|\+|\-|\*|\/|\^|\(|\)',formula )
print(list)
