from sys import argv
script = argv
filename = raw_input("file:")

print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C (^c)."
print "If you do want that,hit RETURN"

# readline ��ȡ�ı��ļ���һ��
# write(stuff)-��stuffд���ļ�
raw_input("?")

print "Opening the file..."
# r:��������w��д������a:��Ӳ�����b:�����ƴ�ȡ���� ���ȱʡ����r
# 'w+' 'r+' 'a+' �ļ�����ͬʱ��д�ķ�ʽ�򿪣����ļ�λ�õ�ʹ����Щ��ͬ
target = open(filename,'w')

print "Truncating the file. Goodbye!"
#���
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