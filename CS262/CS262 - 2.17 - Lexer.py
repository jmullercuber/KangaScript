import ply.lex as lex

tokens = (
  'LANGLE',			# <
  'LANGLESLASH',	# </
  'RANGLE',			# >
  'EQUAL',			# =
  'STRING',			# "hello"
  'WORD',			# Welcome!
)

states = (
    ('htmlcomment', 'exclusive'),	# exclusive, as in that's your ONLY job!
)

t_ignore = ' ' # shortcut for whitespace


# Mode: htmlcomment  --------------------------------------------------------
def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
    r'-->'
    token.lexer.lineno += token.value.count('\n')	# even the newline rule won't be used during a comment
    token.lexer.begin('INITIAL')

def t_htmlcomment_error(token):
    token.lexer.skip(1) # pass



# Mode: INITIAL  --------------------------------------------------------
def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token



# Test it  --------------------------------------------------------
webpage = "hello <!-- comment --> all"

htmllexer = lex.lex()
htmllexer.input(webpage)

while True:
    tok = htmllexer.token()	# returns next token
    if not tok: break		# if no more, then done
    print tok				# display the token


