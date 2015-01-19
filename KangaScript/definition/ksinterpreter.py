# we WILL need KS Data Types
from ksdatatypes import *
# this is it!
# interpret the ast representation of the program




# environment
# ------------------------------------------------
class Environment:
	def __init__(self, parent, book={}):
		self.parent = parent
		self.book = book

global_env = Environment(None, {
		'print' : KS_Function('print', None, None),
		'range' : KS_Function('range', None, None),
	}
)

def env_lookup(vname,env):
	# do I have it?
	if vname in env.book:
		return (env.book)[vname]
	# do I have a parent?
	elif env.parent == None:
		return None
	# ask my parent
	else:
		return env_lookup(vname,env.parent)


def env_update(name, new_value, env):
	# does the variable already exist?
	if env_lookup(name, env) != None:
		env_update_living(name, new_value, env)
	# create and assign value to variable
	else:
		env.book[name] = new_value


def env_update_living(vname,value,env):
        if vname in env.book:
                (env.book)[vname] = value
        elif not (env.parent == None):
                env_update(vname,value,env.parent)




#
# --------------------------------------------------
def interpret(ast, env):
	for element in ast:
		eval_element(element, env)
	# done going through every element
# done interpreting!

def eval_element(element, env):
	etype = element[0]
	# function definition
	if etype == 'function':
		# either named or anonymous
		fvalue = element[1]
		fvalue.setEnv(env)
		env_update(fvalue.name, fvalue, env)
	elif etype == 'compoundstmt':
		eval_compound(element[1], env)
	elif etype == 'simplestmt':
		eval_simple(element[1], env)
	else:
		print "Error: unknown element", element
# done evaluating element

def eval_compound(stmt, env):
	stype = stmt[0]
	
	
	if stype == "if_elselist-otherwise":
		if_else_list = stmt[1]
		otherwise_branch = stmt[2]
		for (name, condition, inards) in if_else_list:
			if eval_exp(condition, env).istrue():
				interpret(inards, env)
				break
		else:
			interpret(otherwise_branch[1], env)

	
	elif stype == "for-in":
		key = stmt[1][1]
		array = eval_exp(stmt[2], env)
		inards = stmt[3]
		# create new env
		forenv = Environment(env, {key:KS_Blank()})
		for i in array.aslist():
			env_update(key, i, forenv)
			try:
				interpret(inards, forenv)
			except KS_Continue as c:
				continue
			except KS_Break as b:
				break
	
	
	elif stype == "while":
		condition = stmt[1]
		inards = stmt[2]
		while eval_exp(condition, env).istrue():
			try:
				interpret(inards, env)
			except KS_Continue as c:
				continue
			except KS_Break as b:
				break
	
	
	else:
		print "Error: unknown compoundstmt", element

def eval_simple(stmt, env):
	stype = stmt[0]
	
	if stype == "continue":
		raise KS_Continue()
	
	
	elif stype == "break":
		raise KS_Break()
	
	
	elif stype == "pass":
		pass
	
	
	elif stype == "return":
		retval = stmt[1]
		# important to evaluate the expression now!
		# otherwise, we could be in the wrong environment
		retval = eval_exp(retval, env)
		raise KS_Return(retval)
	
	
	elif stype == "import":
		pass
	
	
	elif stype == "expression":
		expression = stmt[1]
		eval_exp(expression, env)


	
	else:
		print "Error: unknown simplestmt", stmt, stmt[0]

def eval_exp(exp, env):
	if isinstance(exp, KS_DataType):
		return exp
	
	etype = exp[0]
	
	if etype == "function":
		# don't forget to set the environment!!!
		eval_element(exp, env)

		# return the function now
		return exp[1]
	
	elif etype == "identifier":
		name = exp[1]
#		print "Finding identifier " + name + "....."
		if env.parent != None:
			#print "Env", env.parent.book
			pass
		value = env_lookup(name, env)
		if value == None:
			# either variable declaration, or reference
			
			# assume declaration though
			env_update(name, KS_Blank(), env)
			
#			print "Warning: evaluating identifier " + name + ". First assignment"

			# first assignment, no one can use it yet though. need another operator or future reference
			return None
		else:
			#print "Found identifier", name + ":", value
			#print "value:", value.__string__()
			return value
		#if isinstance(value, KS_Blank):
		#	print "ERROR: unbound variable " + vname
		#else:
		#	return value
	
	
	if etype == "array-concatenation":
		elem = exp[1]
		key = exp[2][1]
		exp_array = eval_exp(exp[3], env).aslist()
		# create new env
		forenv = Environment(env, {key:KS_Blank()})
		# generated array
		gen_array = []
		for e in exp_array:
			env_update(key, e, forenv)
			gen_array += [ eval_exp(e, forenv) ]
		return KS_Array(gen_array)
	
	
	elif etype == "object":
		pair_list = exp[1]
		dictionary = {}
		for (w, k, e) in pair_list:
			dictionary[k] = eval_exp(e, env)
		return KS_Object(dictionary)


	elif etype == "operator_array-rhs":
		array, rhs = exp[1:]
		#print "OPERATOR-ARRAY-RHS", array, rhs
		if rhs[0] == "sublist-stepped":
			start = eval_exp(rhs[1]['start'], env).asnumber()
			end = eval_exp(rhs[1]['end'], env).asnumber()
			step = eval_exp(rhs[1]['step'], env).asnumber()

			if start != None:
				if int(start)!=start:
					print "Error: list indices and step must be integers"
					return None
				else:
					start=int(start)
			
			if end != None:
				if int(end)!=end:
					print "Error: list indices and step must be integers"
					return None
				else:
					end=int(end)
			
			if step != None:
				if int(step)!=step:
					print "Error: list indices and step must be integers"
					return None
				else:
					step=int(step)
			else:
				return KS_Array( array.aslist()[ start : end : step ] )
		elif rhs[0] == "element_at":
			index = eval_exp(rhs[1], env).asnumber()
			#print "ELEMENT-AT", index
			
			if int(index)!=index:
				print "Error: list index"
				return None
			else:
				return array.aslist()[int(index)]


	elif etype == "operator_unary-lhs":
		op = exp[1]
		a = eval_exp(exp[2], env)
		#print "NOTTING", a
		if op == "not":
			return KS_Boolean(not a.istrue())
		else:
			print "Error: unknown operator_unary-lhs", exp


	elif etype == "operator_binary":
		# right now boolean short circuit eval doesn't work
		#print "a", exp[1]
		#print "b", exp[3]
		lhs = exp[1] #eval_exp(exp[1], env)
		op = exp[2]
		rhs = eval_exp(exp[3], env)
		#print "lhs", lhs
		#print "rhs", rhs
		#print "op", op
		
		if (isinstance(lhs, tuple) and lhs[0]=='identifier' and op[-1]=="=" and op!="=="):
			#print "You wanna assign"
			if op == "=":	# Assign_Equal
				env_update(lhs[1], to_KS_DataType( rhs.value ), env)
				return rhs
			
			# lhs op= rhs  -->  lhs = (lhs op rhs)
			#print "Recursive assign"
			currentValue = eval_exp(exp[1], env).value
			if currentValue == None:	# Never defined
				print "Error: never assigned to identifier before. Confusing operation"
			else:
				return eval_exp(
					('operator_binary', lhs, "=", 
						('operator_binary', lhs, op[:-1], rhs)
					),env
					
				)
			#elif op == "+=":	# PLUS_EQUALS
			#	env_update(lhs[1], to_KS_DataType( currentValue + rhs.value ), env)
			#	return rhs
		
		# Only Assign_Equals cared what the original lhs was
		lhs = eval_exp(exp[1], env)
		#print "lhs", lhs
		
		if op == "+":		# PLUS
			return to_KS_DataType( lhs.value + rhs.value )
		elif op == "*":		# TIMES
			return to_KS_DataType( lhs.value * rhs.value )
		elif op == "-":		# MINUS
			return to_KS_DataType( lhs.value - rhs.value )
		elif op == "/":		# DIVIDE
			return to_KS_DataType( lhs.value / rhs.value )
		elif op == "%":		# MODULUS
			return to_KS_DataType( lhs.value % rhs.value )
		elif op == "^":		# EXPONENTIATE
			return to_KS_DataType( lhs.value ** rhs.value )
		
		
		elif op == "and":	# AND
			return to_KS_DataType( lhs.value and rhs.value )
		elif op == "or":	# OR
			return to_KS_DataType( lhs.value or rhs.value )
		
		
		
		elif op == "in":	# IN
			return to_KS_DataType( lhs.value in rhs.value )
		elif op == "has":	# HAS
			return to_KS_DataType( rhs.value in lhs.value  )
		
		
		elif op == ".":		# DOT
		# Doesn't work right now
			if (isinstance(exp[3], tuple) and exp[3][0]=='identifier'):
				key = exp[3][1]
				if (key in lhs.value):
					return lhs.value[key]
				else:
					lhs.value[key] = KS_Blank()
					return lhs.value[key]
		#	if (lhs[0]=='identifier'):
		#		env_update(lhs[1], rhs, env)
		#		return to_KS_DataType( lhs.value[rhs.value] )
		
		
		elif op == "<":		# LT
			return to_KS_DataType( lhs.value < rhs.value )
		elif op == ">":		# GT
			return to_KS_DataType( lhs.value > rhs.value )
		elif op == "<=":	# LT
			return to_KS_DataType( lhs.value <= rhs.value )
		elif op == ">=":	# LT
			return to_KS_DataType( lhs.value >= rhs.value )
		elif op == "==":	# Equal_Equals
			return to_KS_DataType( lhs.value == rhs.value )
		


		# Error, something went wrong at this point
		if (op[-1]=='=' and exp[1][0]=='identifier'):
			print "Error: Attempted assignment to a non-identifier"
		else:
			print "Error: unknown operator_binary", exp


	elif etype == "function-call":
#		print "ENV", env
		#print "exp", exp[1]
#		print "FUNCTION-CALL, finding function defined by expression", exp[1]
		f = eval_exp(exp[1], env)
		fname = f.name
		#fname = exp[1][1]
		#f = eval_exp(fname, env)
		args = exp[2]
#		print "FUNCTION-CALL", f, fname
#		print "ARGS", args
#		print "ARGUMENTS for", fname, "will now be evaluated"
		argvals = [eval_exp(a,env) for a in args]
#		print "ARGUMENTS evaluation for", fname, "done. Evaluation will take place"
		built_in_functions = ['print', 'range']
		if fname in built_in_functions:
			if fname == "print":
				argval = argvals[0]
				#print "PRINTING... exp ... ", argval,env
				#print "ENV", env.book
				print argval.__string__()
				#print "FUNCTION", fname, "done."
			
			elif fname == "range":
				end = argvals[0]
				#print "RANGE... 0 to ... ", end,env
				#print "ENV", env.book
				arr = [
					KS_Number(i)
					for i in
					range(0, int(end.asnumber()))
				]
				print "FUNCTION", fname, "done."
				return KS_Array(arr)
			
		else:
			# find the function
			#f = env_lookup(fname,env)
			#print "ENV", env.book
			#print "FOUND function:", fname, f
			# if it's MIA
			if f == None:
				print "ERROR: call to undefined identifier", fname
			elif not isinstance(f, KS_Function):
				print "ERROR: call to non-function " + fname
			else:
				#f.name, f.params, f.body, f.env
				if len(f.params) <> len(args):
					print "ERROR: wrong number arguments to " + f.name
				else:
					# make a new environment frame
					newenv = Environment(f.env)
					for i in range(len(argvals)):
						# populate it with values
						argval = argvals[i]
						newenv.book[f.params[i][1]] = argval
					# evaluate the body in the new frame
					try:
						interpret(f.body,newenv)
#						print "FUNCTION", fname, "done."
						return KS_Blank()
					except KS_Return as r:
#						print "FUNCTION", fname, "done."
						return r.retval
		# Complicated! 
		
		
		
	else:
		print "Error: unknown expression", exp
