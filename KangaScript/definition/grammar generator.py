import re

productions = []


s = """ks:
	element    ks

element:
	function_definition
	statement_compound
	statement_simple



function_definition:
	FUNCTION    IDENTIFIER    parameters    COLON    element    ENDFUNCTION
	FUNCTION    parameters    COLON    element    ENDFUNCTION

parameters:
	LEFT_PAREN    RIGHT_PAREN
	LEFT_PAREN    param_list    RIGHT_PAREN

param_list:
	EPSILON
	IDENTIFIER
	IDENTIFIER    COMMA    param_list



statement_compound:
	stmt_c_for
	stmt_c_while
	stmt_c_if_group    ENDIF

stmt_c_if_group:
	stmt_c_if
	stmt_c_if    stmt_c_otherwise
	stmt_c_if    stmt_c_elif_block
	stmt_c_if    stmt_c_elif_block    stmt_c_otherwise

stmt_c_for:
	FOR    IDENTIFIER    IN    expression    COLON    element    ENDFOR


stmt_c_while:
	WHILE    expression    COLON    element    ENDWHILE

stmt_c_if:
	IF    expression    COLON    element

stmt_c_otherwise:
	OTHERWISE    COLON    element

stmt_c_elif_block:
	stmt_c_elif    stmt_c_elif_block

stmt_c_elif:
	ELIF    expression    COLON    element


statement_simple:
	stmt_s_control_flow
	stmt_s_import
	stmt_s_expression

stmt_s_control_flow:
	stmt_s_continue
	stmt_s_break
	stmt_s_pass
	stmt_s_return

stmt_s_continue:
	CONTINUE

stmt_s_break:
	BREAK

stmt_s_pass:
	PASS

stmt_s_return:
	RETURN    expression

stmt_s_import:
	IMPORT    dotted_identifier

dotted_identifier:
	IDENTIFIER
	TIMES
	IDENTIFIER    DOT    dotted_identifier

stmt_s_expression:
	expression

expression:
	IDENTIFIER
	literal
	THIS
	LEFT_PAREN    expression    RIGHT_PAREN
	operator_unary_lhs    expression
	expression    operator_rhs_array
	expression    operator_binary    expression
	function_definition
	function_call

function_call:
	IDENTIFIER    LEFT_PAREN    arguments    RIGHT_PAREN

arguments:
	LEFT_PAREN    RIGHT_PAREN
	LEFT_PAREN    exp_list    RIGHT_PAREN

exp_list:
	EPSILON
	expression
	expression    COMMA    exp_list

literal:
	BLANK
	NULL
	TRUE
	FALSE
	STRING_LITERAL
	NUMERIC_LITERAL
	array_literal
	object_literal




array_literal:
	LEFT_BOX    exp_list    RIGHT_BOX
	LEFT_BOX    expression    FOR    IDENTIFIER    IN    expression    RIGHT_BOX

object_literal:
	LEFT_CURLY_BRACE    pair_list    RIGHT_CURLY_BRACE

pair_list:
	EPSILON
	key_value_pair
	key_value_pair    COMMA    pair_list

key_value_pair:
	IDENTIFIER    COLON    expression

operator_unary_lhs:
	operator_unary_lhs_assignment
	operator_unary_lhs_computation

operator_unary_lhs_assignment:
	NOT_EQUALS

operator_unary_lhs_computation:
	NOT

operator_rhs_array:
	expression    LEFT_BOX    array_operator_insides    RIGHT_BOX

array_operator_insides:
	expression
	expression    COLON    expression
	expression    COLON    expression    COLON    expression

operator_binary:
	operator_binary_assignment
	operator_binary_computation
	operator_binary_comparison

operator_binary_assignment:
	ASSIGN_EQUALS
	DOT_EQUALS
	PLUS_EQUALS
	MINUS_EQUALS
	TIMES_EQUALS
	DIVIDE_EQUALS
	MODULUS_EQUALS
	EXPONENT_EQUALS
	AND_EQUALS
	OR_EQUALS

operator_binary_computation:
	DOT
	PLUS
	MINUS
	TIMES
	DIVIDE
	MODULUS
	EXPONENT
	AND
	OR

operator_binary_comparison:
	IN
	HAS
	EQUIVALENCE_EQUAL
	COMPARE_GT
	COMPARE_GTET
	COMPARE_LT
	COMPARE_LTET
"""


# create an array that holds productions and associated rules
for line in s.split("\n"):
	if len(line) == 0:              # empty line
		continue
	elif line[0] != '\t' and line != '':			# new production rule
		name = re.findall(r'.*:', line)[0][:-1]
		p = [name, []]
		productions += [p]
	elif line[0] == '\t':
		p = productions[-1]
		rule = line[1:].replace("    ", " ")
		p[1] += [rule]


# print productions
for (name, rules) in productions:
	print 'def p_' + name + '(p):'
	if len(rules) == 1:
		print '\t\'' + name + ' : ' + rules[0] + '\''
	elif len(rules) > 1:
		print '\t\'\'\'' + name + ' : ' + rules[0]
		for rule in rules[1:-1]:
			print '\t\t| ' + rule
		print '\t\t| ' + rules[-1] + '\'\'\''
	else:
		print '\t\'' + name + ' :\''
	print '\n'
