from sys import argv
script = argv
filename = raw_input("file:")

print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C (^c)."
print "If you do want that,hit RETURN"

# readline 读取文本文件的一行
# write(stuff)-将stuff写入文件
raw_input("?")

print "Opening the file..."
# r:读操作；w：写操作；a:添加操作；b:二进制存取操作 如果缺省就是r
# 'w+' 'r+' 'a+' 文件将以同时读写的方式打开，对文件位置的使用有些不同
target = open(filename,'w')

print "Truncating the file. Goodbye!"
#清空
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "And finally,we close it."
target.close()