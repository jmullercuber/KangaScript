def p_expression_rhsarray(p):
	'expression : expression operator_rhs_array'
	p[0] = ('operator_array-rhs', p[1], p[2])


def p_operator_rhs_array(p):
	'''operator_rhs_array : LEFT_BOX array_operator_insides RIGHT_BOX
		| LEFT_BOX array_operator_insides_missing RIGHT_BOX'''
	p[0] = p[2]

# -----------------------------------------------------------------------


def p_expression_rhsarray(p):
	'''expression : expression LEFT_BOX array_operator_insides RIGHT_BOX
		| expression LEFT_BOX array_operator_insides_missing RIGHT_BOX'''
	p[0] = ('operator_array-rhs', p[1], p[3])

