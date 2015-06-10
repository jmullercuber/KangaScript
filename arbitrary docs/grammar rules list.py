g=[	'''ks : element ks
		| epsilon''',

	'''element : function_definition
		| statement_compound
		| statement_simple''',

	'epsilon :',

	'''function_definition : FUNCTION expression_identifier parameters COLON ks ENDFUNCTION
		| function_anonymous''',

	'''function_anonymous : FUNCTION parameters COLON ks ENDFUNCTION''',

	'''parameters : LEFT_PAREN param_list RIGHT_PAREN''',

	'param_list : epsilon',

	'''param_list : expression_identifier
		| expression_identifier COMMA param_list''',

	'''statement_compound : stmt_c_for
		| stmt_c_while
		| stmt_c_if_group ENDIF''',

	'''stmt_c_if_group : stmt_c_if_F
		| stmt_c_if_FO
		| stmt_c_if_FE
		| stmt_c_if_FEO''',

	'stmt_c_if_F : stmt_c_if',

	'stmt_c_if_FO : stmt_c_if stmt_c_otherwise',

	'stmt_c_if_FE : stmt_c_if stmt_c_elif_block',

	'stmt_c_if_FEO : stmt_c_if stmt_c_elif_block stmt_c_otherwise',

	'stmt_c_for : FOR expression_identifier IN expression COLON ks ENDFOR',

	'stmt_c_while : WHILE expression COLON ks ENDWHILE',

	'stmt_c_if : IF expression COLON ks',

	'stmt_c_otherwise : OTHERWISE COLON ks',

	'''stmt_c_elif_block : stmt_c_elif
		| stmt_c_elif stmt_c_elif_block''',

	'stmt_c_elif : ELIF expression COLON ks',

	'''statement_simple : stmt_s_control_flow
		| stmt_s_import
		| stmt_s_expression''',

	'''stmt_s_control_flow : stmt_s_continue
		| stmt_s_break
		| stmt_s_pass
		| stmt_s_return''',

	'stmt_s_continue : CONTINUE',

	'stmt_s_break : BREAK',

	'stmt_s_pass : PASS',

	'''stmt_s_return : RETURN expression
		| RETURN''',

	'stmt_s_import : IMPORT dotted_identifier',

	'''dotted_identifier : dotted_identifier_something
		| dotted_identifier_everything''',

	'''dotted_identifier_something : expression_identifier
		| expression_identifier DOT dotted_identifier_something''',

	'''dotted_identifier_everything : TIMES
		| dotted_identifier_something DOT TIMES''',

	'stmt_s_expression : expression',

	'expression : literal',

	'expression : function_definition',

	'''expression : LEFT_PAREN expression RIGHT_PAREN''',

	'''expression : NOT_EQUALS expression
		| NOT expression''',

	'''expression : expression LEFT_BOX array_operator_insides RIGHT_BOX
		| expression LEFT_BOX array_operator_missing RIGHT_BOX''',

	'''expression : expression ASSIGN_EQUALS expression
		| expression DOT_EQUALS expression
		| expression PLUS_EQUALS expression
		| expression MINUS_EQUALS expression
		| expression TIMES_EQUALS expression
		| expression DIVIDE_EQUALS expression
		| expression MODULUS_EQUALS expression
		| expression EXPONENT_EQUALS expression
		| expression AND_EQUALS expression
		| expression OR_EQUALS expression
		| expression DOT expression_identifier
		| expression PLUS expression
		| expression MINUS expression
		| expression TIMES expression
		| expression DIVIDE expression
		| expression MODULUS expression
		| expression EXPONENT expression
		| expression AND expression
		| expression OR expression
		| expression IN expression
		| expression HAS expression
		| expression EQUIVALENCE_EQUAL expression
		| expression COMPARE_GT expression
		| expression COMPARE_GTET expression
		| expression COMPARE_LT expression
		| expression COMPARE_LTET expression''',

	'expression : expression_identifier',

	'expression_identifier : IDENTIFIER',

	'expression : THIS',

	'expression : expression LEFT_PAREN exp_list RIGHT_PAREN',

	'exp_list : epsilon',

	'''exp_list : expression
		| expression COMMA exp_list''',

	'''literal : array_literal
		| object_literal
		| literal_string''',

	'literal : BLANK',

	'literal : NULL',

	'literal : TRUE',

	'literal : FALSE',

	'literal_string : STRING_LITERAL',

	'''literal : NUMERIC_LITERAL
		| MINUS NUMERIC_LITERAL''',

	'''array_literal : LEFT_BOX exp_list RIGHT_BOX
		| LEFT_BOX expression FOR expression_identifier IN expression RIGHT_BOX''',

	'object_literal : LEFT_CURLY_BRACE pair_list RIGHT_CURLY_BRACE',

	'''pair_list : epsilon
		| key_value_pair
		| key_value_pair COMMA pair_list''',

	'key_value_pair : literal_string COLON expression',

	'''array_operator_insides : expression
		| expression COLON expression
		| expression COLON expression COLON expression''',

	'''array_operator_missing : expression COLON''',

	'''array_operator_missing : COLON expression''',

	'''array_operator_missing : COLON''',

	'''array_operator_missing : expression COLON COLON expression''',

	'''array_operator_missing : COLON expression COLON expression''',

	'''array_operator_missing : COLON COLON expression''',

	'''array_operator_missing : COLON COLON'''
]
