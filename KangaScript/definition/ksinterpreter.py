# we WILL need KS Data Types
from ksdatatypes import *
# this is it!
# interpret the ast representation of the program



# environment
# ------------------------------------------------
class Environment:
	def __init__(self, parent, book):
		self.parent = parent
		self.book = book
	
	def lookup(self, identifier):
		vname = identifier.name
		# do I have it?
		if vname in self.book:
			return (self.book)[vname]
		# do I have a parent?
		elif self.parent == None:
			return None
		# ask my parent
		else:
			return self.parent.lookup(identifier)
	
	def giveme(self, identifier, new_value=KS_Blank()):
		name = identifier.name
		self.book[name] = new_value
	
	def update(self, identifier, new_value):
		name = identifier.name
		# does the variable already exist?
		if self.lookup(identifier) != None:
			self.update_living(identifier, new_value)
		# create and assign value to variable
		else:
			self.giveme(identifier, new_value)
	
	# sorta private method
	def update_living(self, identifier, value):
		vname = identifier.name
		if vname in self.book:
			self.giveme(identifier, value)
		#elif not (self.parent == None):
		else:
			self.parent.update_living(identifier, value)
	
	def __string__(self):
		return (self.parent, self.book)

# The environment book is a collection of python strings and KS_DataType pairs

global_env = Environment(None, {
		'print' : KS_Function('print', None, None),
		'range' : KS_Function('range', None, None),
	}
)




#
# --------------------------------------------------
def interpret(ast, env):
	for element in ast[:-1]:
		eval_element(element, env)
	# return the value of the last element (:)s for interpretation)
	return eval_element(ast[-1], env)
	# done going through every element
# done interpreting!

def eval_element(element, env):
	# function definition
	if isinstance(element, KS_Function):
		# it'll be either named or anonymous
		fvalue = element
		
		#  set the environment on fvalue from fvalue.env to current env
		fvalue.setEnv(env)
		
		# yes, if you're asking, you should overwrite old value by that name
		# ... if they exist, that is
		# like assignment statement: f = function *anon* () {print(5)}
		# so use the method Environment.update()
		env.update(KS_Identifier(fvalue.name), fvalue)
		return fvalue
	else:
		etype = element[0]
		if etype == 'compoundstmt':
			return eval_compound(element[1], env)
		elif etype == 'simplestmt':
			return eval_simple(element[1], env)
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
		key = stmt[1]
		array = eval_exp(stmt[2], env)
		inards = stmt[3]
		# create new env
		forenv = Environment(env, {key.name:KS_Blank()})
		for i in array.aslist():
			# no don't overwite old values, new scope
			# so Environment.giveme
			forenv.giveme(key, i.primvativesCopy())
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
# done evaluating compound statement

def eval_simple(stmt, env):
	
	if isinstance(stmt, KS_ControlFlow_Interuptive):
		# covers continue, break, and return
		raise stmt
	
	
	
	else:
		stype = stmt[0]
		
		
		if stype == "pass":
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
			return eval_exp(expression, env)
		
		
		else:
			print "Error: unknown simplestmt", stmt, stmt[0]
# done evaluating simple statement

def eval_exp(exp, env):
	#  ....................Made it to eval_exp!!!.............!!!
	if isinstance(exp, KS_Function):
		# don't forget to set the environment!!!
		eval_element(exp, env)
		
		# return the function now
		return exp
	
	elif isinstance(exp, KS_DataType):
		return exp
	
	elif isinstance(exp, KS_Identifier):
		#  >>>>>>>>>>   It's an identifier !!! <<<<<<<<
		name = exp
		#print "Finding identifier " + name + "....."
		if env.parent != None:
			#print "Env", env.parent.book
			pass
		value = env.lookup(name)
		#  -------------'bout that identifier, figured value-------
		if value == None:
			# either variable declaration, or reference
			
			# assume declaration though
			# plop into current environment
			# so Environment.giveme
			env.giveme(name, KS_Blank())
			
			#print "Warning: evaluating identifier " + name.name + ". First assignment"
			
			# first assignment, no one can use it yet though. need another operator or future reference
			return None
		else:
			# strange things happened here....
			# let us not forget it
			
			# Found identifier, name, with value, value
			return value
		#if isinstance(value, KS_Blank):
		#	print "ERROR: unbound variable " + vname
		#else:
		#	return value
	
	etype = exp[0]
	
	if etype == "array-concatenation":
		elem = exp[1]
		key = exp[2]
		exp_array = eval_exp(exp[3], env).aslist()
		# create new env
		forenv = Environment(env, {key.name:KS_Blank()})
		# generated array
		gen_array = []
		for e in exp_array:
			# no don't overwite old values by that name, new scope
			# so Environment.giveme
			forenv.giveme(key, e.primvativesCopy())
			gen_array += [ eval_exp(elem, forenv) ]
		return KS_Array(gen_array)
	
	
	elif etype == "object":
		pair_list = exp[1]
		dictionary = {}
		for (w, k, e) in pair_list:
			dictionary[k] = eval_exp(e, env)
		return KS_Object(dictionary)


	elif etype == "operator_array-rhs":
		array = eval_exp(exp[1], env)
		rhs = exp[2]
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

			return KS_Array( array.aslist()[ start : end : step ] )
		elif rhs[0] == "element_at":
			index = eval_exp(rhs[1], env)
			#print "ELEMENT-AT", index
			
			if ( isinstance(array, KS_Object) ):
				# using array notation to get stuff from an object
				obj = array
				return obj.value[ index ]

			else:
				# using array notation for arrays
				index = index.asnumber()
				if int(index)!=index:
					print "Error: list index"
					return None
				else:
					#print "array", array
					#print "arrayelem", to_KS_DataType(  array.aslist()[int(index)]  )
					return to_KS_DataType(  array.aslist()[int(index)]  )


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
		lhs_id = exp[1]
		op = exp[2]
		rhs_id = exp[3]
		
		
		# Important, interrupt for dot operators
		if op == ".":		# DOT
			return eval_exp_DOT_operator(exp, env)
		
		
		lhs = eval_exp(exp[1], env)
		rhs = eval_exp(exp[3], env)

		#print "lhs", lhs
		#print "rhs", rhs
		#print "op", op
		
		if ( (not isinstance(lhs_id, KS_Identifier)) and op[-1]=='=' and op!="==" and op!=">=" and op!="<="):
			print "Error: Attempted assignment to a non-identifier"
		
		elif (isinstance(lhs_id, KS_Identifier) and op[-1]=="=" and op!="==" and op!=">=" and op!="<="):
			#print "You wanna assign"
			if op == "=":	# Assign_Equal
				#print "rhsassign", lhs, rhs, rhs.__string__()
				# yes, should overwrite old value by that name
				# so Environment.update()
				env.update(lhs_id, rhs)
				return rhs
			
			# lhs op= rhs  -->  lhs = (lhs op rhs)
			else:
				#print "Recursive assign"
				if lhs == None:	# Never defined
					print "Error: never assigned to identifier before. Confusing operation"
				else:
					return eval_exp(
						('operator_binary', lhs_id, "=", 
							('operator_binary', lhs, op[:-1], rhs)
						),env
					)
			#elif op == "+=":	# PLUS_EQUALS
			#	env.update(lhs[1], to_KS_DataType( currentValue + rhs.value ))
			#	return rhs
		
		
		if op == "+":		# PLUS
			return to_KS_DataType( lhs.value + rhs.value )
		elif op == "*":		# TIMES
			#print "lhs, rhs", lhs, rhs, exp[1], exp[3]
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
			#print lhs.value, "in", rhs.value
			return to_KS_DataType( lhs in rhs.value )
		elif op == "has":	# HAS
			return to_KS_DataType( rhs in lhs.value  )
		
		
		elif op == ".":		# DOT
			# same as 'operator_array-rhs' --> 'element_at' --> object

			index = rhs
			
			if ( isinstance(lhs, KS_Object) ):
				if (not(index in lhs.value)):
					# index isn't in object! quick, make it Blank!
					lhs.value[index] = KS_Blank()
				else:
					# index is already defined in there
					pass
				
				return lhs.value[ index ]
			else:
				print "Error: using dot operator, but not on object"
		
		
		elif op == "<":		# LT
			return to_KS_DataType( lhs.value < rhs.value )
		elif op == ">":		# GT
			return to_KS_DataType( lhs.value > rhs.value )
		elif op == "<=":	# LT
			return to_KS_DataType( lhs.value <= rhs.value )
		elif op == ">=":	# LT
			return to_KS_DataType( lhs.value >= rhs.value )
		elif op == "==":	# Equal_Equals
			#print "lhs, rhs", lhs, rhs, exp[1]
			return to_KS_DataType( lhs.value == rhs.value )
		


		# Error, something went wrong at this point
		else:
			print "Error: unknown operator_binary", exp


	elif etype == "function-call":
		# >>>>>>>>>>   It's a function call !!! <<<<<<<<
		# finding function, f, defined by expression, exp[1]
		# if exp[1] is an identifier fname, eval_exp will look it up in env
		# otherwise, exp[1] could be a function definition or other such expression returning KS_Function
		f = eval_exp(exp[1], env)
		
		
		# what if exp wasen't a function!
		# if it's MIA
		if f == None:
			print "ERROR: call to undefined identifier", exp[1]
			return
		# ... or not even a function
		# we have a really, big problem!
		elif not isinstance(f, KS_Function):
			print "ERROR: call to non-function", f.__string__()
			return
		# if exp WAS a function, let's learn its name!
		else:
			fname = f.name
		
		
		# arguments for fname will now be evaluated
		# exp[2] is a list, entries being fname's parameters
		args = exp[2]
		# using array concatenation makes for succinct code
		# create a new list vals, with evaluated/simplified parameters
		argvals = [eval_exp(a,env) for a in args]
		# argument evaluation done
		
		
		# Evaluation will now take place
		
		# Take a look at the built-in functions tho
		built_in_functions = ['print', 'range']
		# if we're calling a built-in, the code implementation is HERE
		if fname in built_in_functions:
			if fname == "print":
				# PRINT every argument in argval
				# hense, array concatenation, and string join
				print ' '.join([e.__string__() for e in argvals])
				return None
				# function fname done.
			
			elif fname == "range":
				# RANGE returns a KS_Array
				# elements being consecutive integers 0 ... to end
				# array concatenation you see
				# PRO: to make it awesome, using to_KS_DataType(  range(blah)  )
				end = argvals[0]
				arr = to_KS_DataType(  range( int(end.asnumber()) )  )
				return arr
				# function fname done.
			
		else:
			# function implementation is not built-in,
			# so use the KS_Function definition
			# it was declared a bit ago as f
			
			# its all good brah!
			
			
			# this is the anatomy of a function
			# in case you forget
			# f.name, f.params, f.body, f.env
			
			# one more possible error... invalid argument count
			if len(f.params) <> len(args):
				print "ERROR: wrong number arguments to " + f.name
			else:
				# make a new environment frame
				# the parent env is based on where the function was declared!!!!!
				# definitely not the current env
				newenv = Environment(f.env, {})
				newenv.parent = f.env  # repetitive???
				
				# populate the new environment with values
				for i in range(len(argvals)):
					# don't overwite old values (like in the parent env(s)) by that name,
					# because values are being declared in new scope
					# so use the method Environment.giveme
					
					# sending copy of simple values,
					# but real thing of complex datatypes,
					# so use the method [KS_DataType].primvativesCopy
					
					newenv.giveme(f.params[i], argvals[i].primvativesCopy())
				
				# do not forget to add 'this' identifier to memory
				# 'this' refers to the function itself
				# don't overwite previous 'this' value, new scope
				# so use the method Environment.giveme
				newenv.giveme(KS_Identifier("this"), f.primvativesCopy())
				
				
				# evaluate the body in the new frame
				try:
					interpret(f.body, newenv)
					# function fname done.
					# default return value is blank
					return KS_Blank()
				
				# if it decides to interrupt and give you a return value
				# extract it, and pass it up
				except KS_Return as r:
					# function fname done.
					return r.retval
		# Complicated! 
		
		
		
	else:
		print "Error: unknown expression", exp
# end evaluating the expression

# this function is for the sole purpose of handeling the binary dot operator
# easily, and away from all the other operators
def eval_exp_DOT_operator(exp, env):
	
	lhs_id = exp[1]
	op = exp[2]
	assert op == "."
	rhs_id = exp[3]
	
	
	lhs = eval_exp(lhs_id, env)
	rhs = rhs_id    # assert isinstance(rhs, KS_Identifier)
	####DO NOT EVAL RHS!!!#####
	
	# replaces from eval_exp(): -->  elif etype == "operator_binary": --> elif op == ".":		# DOT
	# same functionality as 'operator_array-rhs' --> 'element_at' --> object
	
	index = rhs.name
	
	if ( isinstance(lhs, KS_Object) ):
		if (not(index in lhs.value)):
			# index isn't in object! quick, make it Blank!
			lhs.value[index] = KS_Blank()
		else:
			# index is already defined in there
			pass
		
		return lhs.value[ index ]
	else:
		print "Error: using dot operator, but not on object"
	
# done evaluating expression with dot operator
