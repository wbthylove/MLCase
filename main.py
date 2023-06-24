import re
formula = '-1.1-2*((-2+3)+(2/2))'
# 以‘横杠数字’分割，其中正则表达式：(\-\d+\.?\d*) 括号内：
# \-表示匹配横杠开头； \d+ 表示匹配数字1次或多次；\.?表示匹配小数点0次或1次；\d*表示匹配数字0次或多次。
formula_list = [i for i in re.split('(\-\d+\.?\d*)', formula) if i]
# print(formula_list[-1])
for item in formula_list:
    print(item)



