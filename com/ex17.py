from sys import argv
from os.path import exists
# open 与  read返回的对象不同
script = argv
from_file = raw_input("from file:")
to_file = raw_input("to file:")

print "Copying from %s to %s" % (from_file,to_file)

# We could do these two on one line too,how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready,hit RETURN to continue,CRTL-C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright,all done"

out_file.close()
in_file.close()