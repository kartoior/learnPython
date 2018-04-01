from sys import argv
# file.seek(off, whence=0)：从文件中移动off个操作标记（文件指针），正往结束方向移动，负往开始方向移动。如果设定了whence参数，就以whence设定的起始位为准，0代表从头开始，1代表当前位置，2代表文件最末尾位置。
script = argv
input_file = raw_input("input file:")

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)
    
def print_a_line(line_count,f):
    print line_count, f.readline()
    
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now,let's rewind,kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)