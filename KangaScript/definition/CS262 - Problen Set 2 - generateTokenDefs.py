import re

s = """#
	LEFT_PAREN,			# (
	RIGHT_PAREN,		# )
	LEFT_BOX,			# [
	RIGHT_BOX,			# ]
	LEFT_CURLY_BRACE,	# {
	RIGHT_CURLY_BRACE,	# }
	SINGLE_QUOTE,		# \\'
	RIGHT_ARROW,		# ->
	BLANK,				# blank
	NULL,				# null
	TRUE,				# true
	FALSE,				# false
	FUNCTION,			# function
	ENDFUNCTION,		# endfunction
	THIS,				# this
#	IDENTIFIER,			# catch_22, _Apples, Fruit, NOT: 2tea
#	STRING_LITERAL_SQ,	# 'Bob\'s bot grabbled'
#	STRING_LITERAL_DQ,	# "you say \"yes ma'am'\"."
#	NUMERIC_LITERAL,	# 123, 1.45
	COLON,				# :
	FOR,				# for
	WHILE,				# while
	CONTINUE,			# continue
	BREAK,				# break
	PASS,				# pass
	IF,					# if
	ELIF,				# elif
	OTHERWISE, 			# otherwise
	ENDFOR,				# endfor
	ENDWHILE,			# endwhile
	ENDIF,				# endif
	RETURN,				# return
	IN,					# in
	HAS,				# has
	ASSIGN_EQUAL,		# =
	EQUIVALENCE_EQUAL,	# ==
	COMPARE_GT,			# >
	COMPARE_GTET,		# >=
	COMPARE_LT,			# <
	COMPARE_LTET,		# <=
	DOT,				# .
	PLUS,				# +
	MINUS,				# -
	TIMES,				# *
	DIVIDE,				# /
	MODULUS,			# %
	EXPONENT,			# ^
	DOT_EQUALS,			# .=
	PLUS_EQUALS,		# +=
	MINUS_EQUALS,		# -=
	TIMES_EQUALS,		# *=
	DIVIDE_EQUALS,		# /=
	MODULUS_EQUALS,		# %=
	EXPONENT_EQUALS,	# ^=
	AND,				# and
	OR,					# or
	NOT,				# not
	AND_EQUALS,			# &=
	OR_EQUALS,			# |=
	NOT_EQUALS,			# =!"""


r = []
#for line in s.split("\n"):
#	if line[0] != '#':
#		tokenName = re.findall(r'\t.*,', line)[0][1:-1]
#		tokenLook = re.findall(r'# .*', line)[0][2:]
#		
#		tokenDef = "t_" + tokenName + "\t\t= "
#		tokenDef += "r'" + tokenLook + "'"
#		
#		print tokenDef

for line in s.split("\n"):
	if line[0] != '#':
		tokenName = re.findall(r'\t.*,', line)[0][1:-1]
		tokenLook = re.findall(r'# .*', line)[0][2:]
		
		if len(re.findall(r'[a-zA-Z]+', tokenLook)) > 0:
			r += [tokenLook]
		else:
			tokenDef = "t_" + tokenName + "\t\t= "
			tokenDef += "r'" + tokenLook + "'"
			print tokenDef
print r


