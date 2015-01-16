# PLY is the library in use
import ply.yacc as yacc
# requires the token names
from kslexer import tokens

# the goal will be to build an Abstract Syntax Tree (ast) based off the grammar
# no evaluation or optimization will be taking place here
# although evaluation is the technique shown in the PLY calculator example
# I borrow this concept from CS262


# start, precedence
# ------------------------------------------

# starting rule. Tree is rooted here
start = 'ks'

# in the case of an ambiguous expression
# declares what operators to reduce
# lowest to highest
precedence = (
	('left', 'ASSIGN_EQUALS', 'DOT_EQUALS', 'PLUS_EQUALS', 'MINUS_EQUALS', 'TIMES_EQUALS', 'DIVIDE_EQUALS', 'MODULUS_EQUALS', 'EXPONENT_EQUALS', 'AND_EQUALS', 'OR_EQUALS', 'NOT_EQUALS'),
	('left', 'OR'),
	('left', 'AND'),
	('left', 'EQUIVALENCE_EQUAL', 'COMPARE_LT', 'COMPARE_LTET', 'COMPARE_GT', 'COMPARE_GTET'),
	('left', 'IN', 'HAS'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE', 'MODULUS'),
	('left', 'EXPONENT'),
	('right', 'NOT'),
	('left', 'DOT'),
)


# production rules
# -----------------------------------------------
def p_ks(p):
	'''ks : element ks
		| epsilon'''
	if len(p)==2:
		p[0] = p[1]
	elif len(p)==3:
		p[0] = [p[1]] + p[2]


def p_element(p):
	'''element : function_definition
		| statement_compound
		| statement_simple'''
	p[0] = p[1]


def p_epsilon(p):
	'epsilon :'
	p[0] = []


def p_function_definition(p):
	'''function_definition : FUNCTION IDENTIFIER parameters COLON ks ENDFUNCTION
		| function_anonymous'''
	if len(p)==7:
		p[0] = ('function', p[2], p[3], p[5])
	elif len(p)==2:
		p[0] = p[1]

def p_function_anonmyous(p):
	'''function_anonymous : FUNCTION parameters COLON ks ENDFUNCTION'''
	p[0] = ('function', '*anon*', p[2], p[4])
	

def p_parameters(p):
	'''parameters : LEFT_PAREN param_list RIGHT_PAREN'''
	#if len(p) == 3:
	#	p[0] = []
	#elif len(p) == 4:
	p[0] = p[2]

def p_param_list_empty(p):
	'param_list : epsilon'
	p[0] = p[1]

def p_param_list_stuff(p):
	'''param_list : IDENTIFIER
		| IDENTIFIER COMMA param_list'''
	if len(p)==4:
		p[0] = [p[1]] + p[3]
	elif len(p)==2:
		p[0] = [p[1]]

def p_statement_compound(p):
	'''statement_compound : stmt_c_for
		| stmt_c_while
		| stmt_c_if_group ENDIF'''
	p[0] = ('compoundstmt', p[1])


def p_stmt_c_if_group(p):
	'''stmt_c_if_group : stmt_c_if_F
		| stmt_c_if_FO
		| stmt_c_if_FE
		| stmt_c_if_FEO'''
	p[0] = p[1]

def p_stmt_c_if_F(p):
	'stmt_c_if_F : stmt_c_if'
	p[0] = ('if-elselist-otherwise', p[1], [], [])

def p_stmt_c_if_FO(p):
	'stmt_c_if_FO : stmt_c_if stmt_c_otherwise'
	p[0] = ('if-elselist-otherwise', p[1], [], p[2])

def p_stmt_c_if_FE(p):
	'stmt_c_if_FE : stmt_c_if stmt_c_elif_block'
	p[0] = ('if-elselist-otherwise', p[1], p[2], [])

def p_stmt_c_if_FEO(p):
	'stmt_c_if_FEO : stmt_c_if stmt_c_elif_block stmt_c_otherwise'
	p[0] = ('if-elselist-otherwise', p[1], p[2], p[3])


def p_stmt_c_for(p):
	'stmt_c_for : FOR IDENTIFIER IN expression COLON ks ENDFOR'
	p[0] = ('for-in', p[2], p[4], p[6])


def p_stmt_c_while(p):
	'stmt_c_while : WHILE expression COLON ks ENDWHILE'
	p[0] = ('while', p[2], p[4])


def p_stmt_c_if(p):
	'stmt_c_if : IF expression COLON ks'
	p[0] = ('if', p[2], p[4])


def p_stmt_c_otherwise(p):
	'stmt_c_otherwise : OTHERWISE COLON ks'
	p[0] = ('otherwise', p[3])

def p_stmt_c_elif_block(p):
	'''stmt_c_elif_block : stmt_c_elif
		| stmt_c_elif stmt_c_elif_block'''
	if len(p)==2:
		p[0] = [p[1]]
	elif len(p)==3:
		p[0] = [p[1]] + p[3]

def p_stmt_c_elif(p):
	'stmt_c_elif : ELIF expression COLON ks'
	p[0] = ('elif', p[2], p[4])

def p_statement_simple(p):
	'''statement_simple : stmt_s_control_flow
		| stmt_s_import
		| stmt_s_expression'''
	p[0] = ('simplestmt', p[1])


def p_stmt_s_control_flow(p):
	'''stmt_s_control_flow : stmt_s_continue
		| stmt_s_break
		| stmt_s_pass
		| stmt_s_return'''
	p[0] = p[1]


def p_stmt_s_continue(p):
	'stmt_s_continue : CONTINUE'
	p[0] = ('continue')


def p_stmt_s_break(p):
	'stmt_s_break : BREAK'
	p[0] = ('break')

def p_stmt_s_pass(p):
	'stmt_s_pass : PASS'
	p[0] = ('pass')

def p_stmt_s_return(p):
	'''stmt_s_return : RETURN expression
		| RETURN'''
	if len(p)==3:
		p[0] = ('return', p[2])
	elif len(p)==2:
		p[0] = ('return', ("blank"))

def p_stmt_s_import(p):
	'stmt_s_import : IMPORT dotted_identifier'
	p[0] = ('import', p[2])

def p_dotted_identifier(p):
	'''dotted_identifier : IDENTIFIER
		| TIMES
		| IDENTIFIER DOT dotted_identifier'''
	if len(p)==4:
		p[0] = [p[1]] + p[3]
	elif len(p)==2:
		p[0] = [p[1]]

def p_stmt_s_expression(p):
	'stmt_s_expression : expression'
	p[0] = ('expression', p[1])


def p_expression_literal(p):
	'expression : literal'
	p[0] = p[1]


def p_expression_function(p):
	'''expression : function_anonymous
		| function_call'''
	p[0] = p[1]


def p_expression_paren(p):
	'''expression : LEFT_PAREN expression RIGHT_PAREN'''
	p[0] = p[2]


def p_expression_unarylhs(p):
	'expression : operator_unary_lhs expression'
	p[0] = ('operator_unary-lhs', p[1], p[2])


def p_expression_rhsarray(p):
	'expression : expression operator_rhs_array'
	p[0] = ('operator_array-rhs', p[1], p[2])


def p_expression_binary(p):
	'expression : expression operator_binary expression'
	p[0] = ('operator_binary', p[1], p[2], p[3])


def p_expression_identifier(p):
	'expression : IDENTIFIER'
	p[0] = ('identifier', p[1])

def p_expression_this(p):
	'expression : THIS'
	p[0] = ("identifier", 'this')

def p_function_call(p):
	'function_call : IDENTIFIER arguments'
	p[0] = ('function-call', p[1], p[3])

def p_arguments(p):
	'''arguments : LEFT_PAREN exp_list RIGHT_PAREN'''
	p[0] = p[2]


def p_exp_list_empty(p):
	'exp_list : epsilon'
	p[0] = p[1]

def p_exp_list(p):
	'''exp_list : expression
		| expression COMMA exp_list'''
	if len(p)==4:
		p[0] = [p[1]] + p[3]
	elif len(p)==2:
		p[0] = [p[1]]


def p_literal(p):
	'''literal : array_literal
		| object_literal'''
	p[0] = p[1]


## interrupt
def p_literal_blank(p):
	'literal : BLANK'
	p[0] = ("blank",)

def p_literal_null(p):
	'literal : NULL'
	p[0] = ("null",)

def p_literal_true(p):
	'literal : TRUE'
	p[0] = ("true",)

def p_literal_false(p):
	'literal : FALSE'
	p[0] = ("false",)

def p_literal_string(p):
	'literal : STRING_LITERAL'
	p[0] = ("string", p[1])

def p_literal_number(p):
	'literal : NUMERIC_LITERAL'
	p[0] = ("number", p[1])
## end interrupt


def p_array_literal(p):
	'''array_literal : LEFT_BOX exp_list RIGHT_BOX
		| LEFT_BOX expression FOR IDENTIFIER IN expression RIGHT_BOX'''
	if len(p)==4:
		p[0] = ('array', p[2])
	elif len(p)==8:
		p[0] = ('array-concatenation', p[2], p[4], p[6])


def p_object_literal(p):
	'object_literal : LEFT_CURLY_BRACE pair_list RIGHT_CURLY_BRACE'
	p[0] = ('object', p[2])


def p_pair_list(p):
	'''pair_list : epsilon
		| key_value_pair
		| key_value_pair COMMA pair_list'''
	if len(p)==4:
		p[0] = p[1] + p[3]
	elif len(p)==2:
		p[0] = p[1]

def p_key_value_pair(p):
	'key_value_pair : IDENTIFIER COLON expression'
	p[0] = [('key_value_pair', p[1], p[3])]


def p_operator_unary_lhs(p):
	'''operator_unary_lhs : operator_unary_lhs_assignment
		| operator_unary_lhs_computation'''
	p[0] = p[1]

def p_operator_unary_lhs_assignment(p):
	'operator_unary_lhs_assignment : NOT_EQUALS'
	p[0] = p[1]

def p_operator_unary_lhs_computation(p):
	'operator_unary_lhs_computation : NOT'
	p[0] = p[1]

def p_operator_rhs_array(p):
	'operator_rhs_array : LEFT_BOX array_operator_insides RIGHT_BOX'
	p[0] = p[2]

def p_array_operator_insides(p):
	'''array_operator_insides : expression
		| expression COLON expression
		| expression COLON expression COLON expression'''
	if len(p)==6:
		p[0] = ('sublist-stepped', p[1], p[3], p[5])
	elif len(p)==4:
		p[0] = ('sublist-stepped', p[1], p[3], ("number", 1))
	elif len(p)==2:
		p[0] = ('element_at', p[1])

def p_operator_binary(p):
	'''operator_binary : operator_binary_assignment
		| operator_binary_computation
		| operator_binary_comparison'''
	p[0] = p[1]

def p_operator_binary_assignment(p):
	'''operator_binary_assignment : ASSIGN_EQUALS
		| DOT_EQUALS
		| PLUS_EQUALS
		| MINUS_EQUALS
		| TIMES_EQUALS
		| DIVIDE_EQUALS
		| MODULUS_EQUALS
		| EXPONENT_EQUALS
		| AND_EQUALS
		| OR_EQUALS'''
	p[0] = p[1]

def p_operator_binary_computation(p):
	'''operator_binary_computation : DOT
		| PLUS
		| MINUS
		| TIMES
		| DIVIDE
		| MODULUS
		| EXPONENT
		| AND
		| OR'''
	p[0] = p[1]

def p_operator_binary_comparison(p):
	'''operator_binary_comparison : IN
		| HAS
		| EQUIVALENCE_EQUAL
		| COMPARE_GT
		| COMPARE_GTET
		| COMPARE_LT
		| COMPARE_LTET'''
	p[0] = p[1]



# errors - they're gonna happen'
# ---------------------
def p_error(p):
    print("Syntax error at '%s'" % p.value)



# build the lexer
# -----------------------------------------------

parser = yacc.yacc()
