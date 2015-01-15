# PLY is the library in use
import ply.lex as lex

# declare what tokens will exist

tokens = (
	# Punctuation
	LEFT_PAREN,			# (
	RIGHT_PAREN,		# )
	LEFT_BOX,			# [
	RIGHT_BOX,			# ]
	LEFT_CURLY_BRACE,	# {
	RIGHT_CURLY_BRACE,	# }
	SINGLE_QUOTE,		# '
	RIGHT_ARROW,		# ->        # idk, want some way for short anon functions
	
	# Values
	BLANK,				# blank
	NULL,				# null
	TRUE,				# true
	FALSE,				# false
	FUNCTION,			# function
	ENDFUNCTION,		# endfunction
	THIS,				# this
	IDENTIFIER,			# catch_22, _Apples, Fruit, NOT: 2tea
	
	STRING_LITERAL_SQ,	# 'Bob\'s bot grabbled'
	STRING_LITERAL_DQ,	# "you say \"yes ma'am'\"."
	NUMERIC_LITERAL,	# 123, 1.45
	
	# Compound statements
	COLON,				# :
	FOR,				# for
	WHILE,				# while
	CONTINUE,			# continue
	BREAK,				# break
	PASS,				# pass
	IF,					# if
	ELIF,				# elif
	OTHERWISE, 			# otherwise            # just because
	ENDFOR,				# endfor
	ENDWHILE,			# endwhile
	ENDIF,				# endif
	RETURN,				# return                # how about "~" ?
	# try - catch/except - finally
	
	# Operators
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
	NOT_EQUALS,			# =!
)
