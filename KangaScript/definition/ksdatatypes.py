# data types
# ------------------------------------------------

class KS_DataType:
	def istrue(self):
		return false
	def aslist(self):
		return None
	def asnumber(self):
		return 0
	def __string__(self):
		return ''
	pass


# gotta have my pops!
# jking, gotta have a representation for identifiers
class KS_Identifier():
	def __init__(self, name):
		self.name = name
	#	self.env = env
	#def istrue(self):
	#	return len(self.value) > 0
	#def aslist(self):
	#	return list(self.value)
	#def asnumber(self):
	#	return int(self.value)
	#def __string__(self):
	#	return self.value

# representing the Blank/undefined but not null data type
class KS_Blank(KS_DataType):
	def istrue(self):
		return false

# representing the null (i don''t have a clue) data type
class KS_Null(KS_DataType):
	def istrue(self):
		return false
	def asnumber(self):
		return None
	def __string__(self):
		return None

class KS_Function(KS_DataType):
	def __init__(self, name, params, body, env=None):
		self.name = name
		self.params = params
		self.body = body
		self.env = env
	def setEnv(self, env):
		self.env = env
	def istrue(self):
		return True
	def __string__(self):
		return 'Function ' + self.name

class KS_Boolean(KS_DataType):
	def __init__(self, value):
		self.value = value
	def istrue(self):
		return self.value
	def asnumber(self):
		return 1 if self.value else 0
	def __string__(self):
		return 'true' if self.value else 'false'

class KS_Number(KS_DataType):
	def __init__(self, value):
		self.value = value
	def istrue(self):
		return self.value != 0
	def asnumber(self):
		return self.value
	def __string__(self):
		return str(self.value)

class KS_String(KS_DataType):
	def __init__(self, value):
		self.value = value
	def istrue(self):
		return len(self.value) > 0
	def aslist(self):
		return list(self.value)
	def asnumber(self):
		return int(self.value)
	def __string__(self):
		return "'" + self.value + "'"

class KS_Object(KS_DataType):
	def __init__(self, value):
		self.value = value
	def istrue(self):
		return True
	def aslist(self):
		return self.value.keys()
	def asnumber(self):
		return 1
	def __string__(self):
		return 'KS_Object ' + str(self.value)

class KS_Array(KS_DataType):
	def __init__(self, value):
		self.value = value
	def istrue(self):
		return True
	def aslist(self):
		return self.value
	def asnumber(self):
		return len(self.value)
	def __string__(self):
		return str([e.__string__() for e in self.value])

def to_KS_DataType(x):
#	print "TO-KS-DATATYPE", x
	if isinstance(x, KS_DataType):
		return x
	if (type(x) is int) or (type(x) is float):
		return KS_Number(x)
	elif (type(x) is str):
		return KS_String(x)
	elif (type(x) is bool):
		return KS_Boolean(x)
	elif (type(x) is list):
		return KS_Array(x)
	elif (type(x) is dict):
		return KS_Object(x)
	else:
		return KS_Null()


# Control Flow Exceptiond
# ----------------------------------
class KS_Return(Exception):
	def __init__(self, retval):
		self.retval = retval

class KS_Continue(Exception):
	def __init__(self, label=None):
		self.label = label

class KS_Break(Exception):
	def __init__(self, label=None):
		self.label = label

