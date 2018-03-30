# 出现编译错误问题 需在第一行加上 #coding=utf-8
# row_input() 的功能
# 1. 输入字符串

raw_input_A = raw_input("raw input:")
type(raw_input_A)

# 2.输入整数
raw_input_B = raw_input("input int:")
type(raw_input_B)

# 3.输入浮点数
raw_input_C = raw_input("input a float:")
type(raw_input_C)

#可以看到raw_input()函数将用户输入的任意类型数据都转换为一个字符串
#input（）函数要求用户输入有效的表达式

print "How old are you?",
age = raw_input()
print "How tall are you",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

input(3 + 8)
raw_input(3 + 8)