# PLY is the library in use
import ply.lex as lex



# declare what tokens will exist

tokens = (
	# Punctuation
	'LEFT_PAREN',			# (
	'RIGHT_PAREN',			# )
	'LEFT_BOX',				# [
	'RIGHT_BOX',			# ]
	'LEFT_CURLY_BRACE',		# {
	'RIGHT_CURLY_BRACE',	# }
	'COMMA',				# ,
	#'SINGLE_QUOTE',		# '			# no use so far
	'RIGHT_ARROW',			# ->        # idk, want some way for short anon functions
	
	# Values
	'BLANK',				# blank
	'NULL',					# null
	'TRUE',					# true
	'FALSE',				# false
	'FUNCTION',				# function
	'ENDFUNCTION',			# endfunction
	'THIS',					# this
	'IDENTIFIER',			# catch_22, _Apples, Fruit, NOT: 2tea
	
	#'STRING_LITERAL_SQ',	# 'Bob\'s bot grabbled'
	#'STRING_LITERAL_DQ',	# "you say \"yes ma'am'\"."
	'STRING_LITERAL',		# token name for both of them
	'NUMERIC_LITERAL',		# 123, 1.45
	
	# Compound statements
	'COLON',				# :
	'FOR',					# for
	'WHILE',				# while
	'CONTINUE',				# continue
	'BREAK',				# break
	'PASS',					# pass
	'IMPORT',				# import
	'IF',					# if
	'ELIF',					# elif
	'OTHERWISE', 			# otherwise
	'ENDFOR',				# endfor
	'ENDWHILE',				# endwhile
	'ENDIF',				# endif
	'RETURN',				# return
	# try - catch/except - finally
	
	# Operators
	'IN',					# in
	'HAS',					# has
	
	'ASSIGN_EQUALS',		# =
	
	'EQUIVALENCE_EQUAL',	# ==
	'COMPARE_GT',			# >
	'COMPARE_GTET',			# >=
	'COMPARE_LT',			# <
	'COMPARE_LTET',			# <=
	
	'DOT',					# .
	'PLUS',					# +
	'MINUS',				# -
	'TIMES',				# *
	'DIVIDE',				# /
	'MODULUS',				# %
	'EXPONENT',				# ^
	
	'DOT_EQUALS',			# .=
	'PLUS_EQUALS',			# +=
	'MINUS_EQUALS',			# -=
	'TIMES_EQUALS',			# *=
	'DIVIDE_EQUALS',		# /=
	'MODULUS_EQUALS',		# %=
	'EXPONENT_EQUALS',		# ^=
	
	'AND',					# and
	'OR',					# or
	'NOT',					# not
	
	'AND_EQUALS',			# &=
	'OR_EQUALS',			# |=
	'NOT_EQUALS',			# =!
)



# lexer states

states = (
	#('comment', 'exclusive'),   # so far, no multi-line comments i'm worrying about
)


# token definitions
# -----------------------------------------

# end of line comment
# not in token list because program discards them
# hense, pass statement
def t_ignore_eolcomment(t):
	r'\#.*'
	pass



# reserved keywords
# it's importatnt to have these here because
# they look like identifiers
# instead of making rules for each of them
# they'll just piggy off identifiers
reserved = ['blank', 'null', 'true', 'false', 'function', 'endfunction', 'this', 'for', 'while', 'continue', 'break', 'pass', 'import', 'if', 'elif', 'otherwise', 'endfor', 'endwhile', 'endif', 'return', 'in', 'has', 'and', 'or', 'not']



# identifiers and literals
# these are a combination of
# alphanumeric sybols amoung others
# only these tokens have alphanumberic symbols
def t_IDENTIFIER(token):
	r'[A-Za-z_][A-Za-z_0-9]*'
	if token.value in reserved:		# this is where reserved words start piggy-backing
		token.type = token.value.upper()
	return token

def t_STRING_LITERAL_SQ(token):
	r"\'(?:[^'\\]|[\\.])*\'"
	token.type = "STRING_LITERAL"		# declare type as general STRING_LITERAL token. no difference
	token.value = token.value[1:-1]
	return token

def t_STRING_LITERAL_DQ(token):
	r'\"(?:[^"\\]|[\\.])*\"'
	token.type = "STRING_LITERAL"
	token.value = token.value[1:-1]
	return token

def t_NUMERIC_LITERAL_FLOAT(token):
	r'[0-9]*\.[0-9]+'
	token.type = "NUMERIC_LITERAL"
	token.value = float(token.value)
	return token

def t_NUMERIC_LITERAL_INT(token):
	r'[0-9]+'
	token.type = "NUMERIC_LITERAL"
	token.value = int(token.value)
	return token



# symbolic rules
# ordering of tokens differs from documentation
# becuase tokens have over lapping definitions
# ex. ==, = = or +=, + =
# easily identify what is matched first
# using PLY, not necessary, sorts by length anyway
t_LEFT_PAREN				= r'\('
t_RIGHT_PAREN				= r'\)'
t_LEFT_BOX					= r'\['
t_RIGHT_BOX					= r'\]'
t_LEFT_CURLY_BRACE			= r'\{'
t_RIGHT_CURLY_BRACE			= r'\}'
t_COMMA						= r'\,'
#t_SINGLE_QUOTE				= r'\''
t_RIGHT_ARROW				= r'\-\>'
t_COLON						= r'\:'
t_EQUIVALENCE_EQUAL			= r'\=\='
t_COMPARE_GTET				= r'\>\='
t_COMPARE_LTET				= r'\<\='
t_DOT_EQUALS				= r'\.\='
t_PLUS_EQUALS				= r'\+\='
t_MINUS_EQUALS				= r'\-\='
t_TIMES_EQUALS				= r'\*\='
t_DIVIDE_EQUALS				= r'\/\='
t_MODULUS_EQUALS			= r'\%\='
t_EXPONENT_EQUALS			= r'\^\='
t_AND_EQUALS				= r'\&\='
t_OR_EQUALS					= r'\|\='
t_NOT_EQUALS				= r'\=\!'
t_COMPARE_GT				= r'\>'
t_COMPARE_LT				= r'\<'
t_DOT						= r'\.'
t_PLUS						= r'\+'
t_MINUS						= r'\-'
t_TIMES						= r'\*'
t_DIVIDE					= r'\/'
t_MODULUS					= r'\%'
t_EXPONENT					= r'\^'
t_ASSIGN_EQUALS				= r'\='



# newlines, whitespace, and illegal character rules
# --------------------------------------------

# newline
# this will help the lexer know what line of code we are on
def t_newline(token):
	r'\n+'
	token.lexer.lineno += len(token.value)
	pass

# whitespace
# the lexer should completely ignore these characters.
t_ignore = ' \t\v\r'

# illegal character error
# print that there was a bad character
# and move on to the next character of input
def t_error(token):
	print "Illegal character:", token.value[0]
	print "@ line no", token.lexer.lineno
	token.lexer.skip(1)



# build the lexer
# -----------------------------------------------

lexer = lex.lex()
