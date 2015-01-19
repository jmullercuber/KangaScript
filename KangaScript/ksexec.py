# I'll need this to use command arguments
import sys, os.path
# let's get the one instance of the KS Parser
from definition.ksparser import parser
from definition.ksinterpreter import interpret, global_env

# make sure to get the correct CL arguments
if len(sys.argv) != 2 and len(sys.argv) != 3 :
	print "Usage: exec.py [FILE] [-e]"
	quit(1)

# the file location we want
ksfile = sys.argv[1]
ksstring = ""

if len(sys.argv) == 2:
	# make sure argument actually is a file
	if not os.path.isfile(ksfile):
		print "File", ksfile, "Does not exist"
		print "Usage: exec.py [FILE] [-e]"
		quit(1)
		
	# get the file into a string to read
	with open(ksfile, "r") as myfile:
	    ksstring = myfile.read()

elif len(sys.argv) == 3:
	switch = sys.argv[2]
	if switch != "-e":
		print "Usage: exec.py [FILE] [-e]"
	ksstring = ksfile


print ksstring
ast = parser.parse(ksstring)
#print ast
interpret(ast, global_env)
