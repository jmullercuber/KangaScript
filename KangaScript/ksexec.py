#!/usr/bin/env python

# I'll need this to use command arguments
import argparse
import os
# let's get the one instance of the KS Parser
from definition.ksparser import parser as ksparser
from definition.ksinterpreter import interpret as ksinterpret
from definition.ksinterpreter import GlobalEnv
from definition.ksdatatypes import KS_Blank
from ksinteractive import ks_interactive, interpreter_intro_text

##############  ARG PARSE STUFF HERE  #################
# Create the command line argument parser
cl_parser = argparse.ArgumentParser(description='Execute KangaScript programs.')

# Add arguments to look for
# i, Interactive Mode
cl_parser.add_argument('-i', '--interactive', action='store_true', dest='interactive_mode', required=False)

# s, Show Source
cl_parser.add_argument('-s', '--show_source', action='store_true', dest='show_source', required=False)

# String or file argument group
script_group = cl_parser.add_mutually_exclusive_group()

# e, Execute String
script_group.add_argument('-e', '--execute', type=str, action='store', dest='ksstring')

# f/F, filename
script_group.add_argument('-f', '-F', '--file', action='store', type=argparse.FileType('r'), dest='ksfile')

# filename, -f switch above is optional
# store to different variable KSFILE (in caps)
script_group.add_argument('KSFILE', action='store', type=argparse.FileType('r'), nargs="?")


# Evaluate Args
cl_args = cl_parser.parse_args()

# Act with those arguments!
## Determine the ks script
## Evaluate the script
## If interactive, stay open

## Determine the ks script
ksfile = cl_args.ksfile or cl_args.KSFILE
if ksfile:
	# stuff to execute is in file stored in ksfile arg
	cl_args.ksstring = ksfile.read()
	ksfile.close()
elif not cl_args.ksstring:  # no arguments, interactive mode
	# nothing presented to user yet, print welcome message
	print(interpreter_intro_text)
	ks_interactive()
	quit(1)
else:
	# stuff to execute is already stored in ksstring arg
	pass
# end if gettting the ks string

##############  ARG PARSE STUFF HERE  #################

# Determine to echo source
if cl_args.show_source:
	print cl_args.ksstring
	print "#"*10 + "EOF" + "#"*10
	print ""
# end if determining whether to echo source


## Evaluate the script
try:
    ks_global_env = GlobalEnv( os.getcwd() ) # TODO: Update pwd param with file's parent dir
    ast = ksparser.parse(cl_args.ksstring)
    res = ksinterpret(ast, ks_global_env)
    if res != None and not isinstance(res, KS_Blank):
        print res
    # showing the result
except SyntaxError:
    # syntax errors already taken care of in parser
    pass
# end try-except handeling KangaScript syntax errors


## If interactive, stay open
if not cl_args.interactive_mode:
	# formal exit
	raw_input("Press Enter to Exit")
	quit(1)
# end if determining what to do if NOT interactive

# if this far, is interactive!
ks_interactive()
