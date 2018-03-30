# 出现编译错误问题 需在第一行加上 #coding=utf-8
# 整数的输出
# %o --oct 八进制
# %d --dec 十进制
# %x --hex 十六进制 %X  十六进制整数大写
# %i --整数
# %u --无符号整数


# 浮点数输出
# %f --保留小数点后面六位有效数字    %.3f --保留三位小数位
# %e --保留小数点后面六位有效数字，指数形式输出   %.3e --保留三位小数位,实用科学计数法
# %g --在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法   %.3g，保留3位有效数字，使用小数或科学计数法 

# %c --字符
# 字符串输出
# %s  %10s——右对齐，占位符10位 %-10s——左对齐，占位符10位  %.2s——截取2位字符串  %10.2s——10位占位符，截取两位字符串
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those %s." % (binary,do_not)

print x
print y

print "I said: %r" % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side"

print w + e