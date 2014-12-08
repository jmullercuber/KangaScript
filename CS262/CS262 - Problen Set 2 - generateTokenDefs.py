import re

s = """'ANDAND',       # &&
        'COMMA',        # ,
        'DIVIDE',       # /
        'ELSE',         # else
        'EQUAL',        # =
        'EQUALEQUAL',   # ==
        'FALSE',        # false
        'FUNCTION',     # function
        'GE',           # >=
        'GT',           # >
#       'IDENTIFIER',   #### Not used in this problem.
        'IF',           # if
        'LBRACE',       # {
        'LE',           # <=
        'LPAREN',       # (
        'LT',           # <
        'MINUS',        # -
        'NOT',          # !
#       'NUMBER',       #### Not used in this problem.
        'OROR',         # ||
        'PLUS',         # +
        'RBRACE',       # }
        'RETURN',       # return
        'RPAREN',       # )
        'SEMICOLON',    # ;
#       'STRING',       #### Not used in this problem. 
        'TIMES',        # *
        'TRUE',         # true
        'VAR',          # var"""

for line in s.split("\n"):
	if line[0] != '#':
		tokenName = re.findall(r'\'.*\'', line)[0][1:-1]
		tokenLook = re.findall(r'# .*', line)[0][2:]
		
		tokenDef = "def t_" + tokenName + "(token):\n"
		tokenDef += (" "*8) + "r'" + tokenLook + "'\n"
		tokenDef += (" "*8) + "return token"
		
		print tokenDef + ("\n")

