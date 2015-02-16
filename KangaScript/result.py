#function F(n):
#	if n == 0:
#		return 0
#	elif n == 1:
#		return 1
#	otherwise:
#		return F(n-1) + F(n-2)
#	endif
#endfunction

#for i in range(10):
#	print ( F(i) )
#endfor

space = 0

function f(x):
	space += 1
	print("  "*space + "Welcome to f with", x)
	if x<=1:
		print("  "*space + "x is too small, returning 1")
		space -= 1
		return 1
	otherwise:
		print("  "*space + "x is big enough", x)
		#print("  "*space + "before we define it, what is y?", y)
		y = x-1
		print("  "*space + "before we find a, let's check up on y. It is ", y)
		a = 2*f(y)
		print("  "*space + "a is ", a)
		print("  "*space + "before we find b, let's check up on y. It is ", y)
		b = 3*f(y)
		print("  "*space + "b is ", b)
		print("  "*space + "a is ", a, " and b is ", b)
		print("  "*space + "result is ", a+b)
		space -= 1
		return a+b
	endif
endfunction

print( f(5) )

##########EOF##########

Warning: evaluating identifier space. First assignment
CALLING SETENV. BY interpret ON f FROM None TO <definition.ksinterpreter.Environment instance at 0x01F9C940>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM None TO <definition.ksinterpreter.Environment instance at 0x01F9C940>
CALLING SETENV. BY eval_exp ON print FROM None TO <definition.ksinterpreter.Environment instance at 0x01F9C940>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM None TO <definition.ksinterpreter.Environment instance at 0x01F9C940>
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x01F9C940> TO <definition.ksinterpreter.Environment instance at 0x01F9C940>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x01F9C940> TO <definition.ksinterpreter.Environment instance at 0x01F9C940>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x01F9C940> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x01F9C940> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
  Welcome to f with 5
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
  x is big enough 5
Warning: evaluating identifier y. First assignment
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
  before we find a, let's check up on y. It is  4
Warning: evaluating identifier a. First assignment
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x01F9C940> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x01F9C940> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
    Welcome to f with 4
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
    x is big enough 4
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
    before we find a, let's check up on y. It is  3
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
      Welcome to f with 3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
      x is big enough 3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
      before we find a, let's check up on y. It is  2
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
        Welcome to f with 2
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
        x is big enough 2
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
        before we find a, let's check up on y. It is  1
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B96C0>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B96C0>
          Welcome to f with 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B96C0> TO <definition.ksinterpreter.Environment instance at 0x020B96C0>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B96C0> TO <definition.ksinterpreter.Environment instance at 0x020B96C0>
          x is too small, returning 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B96C0> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B96C0> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
        a is  2
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
        before we find b, let's check up on y. It is  1
Warning: evaluating identifier b. First assignment
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9990>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9990>
          Welcome to f with 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9990> TO <definition.ksinterpreter.Environment instance at 0x020B9990>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9990> TO <definition.ksinterpreter.Environment instance at 0x020B9990>
          x is too small, returning 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9990> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9990> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
        b is  3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
        a is  2  and b is  3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9620>
        result is  5
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
      a is  10
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
      before we find b, let's check up on y. It is  1
Warning: evaluating identifier b. First assignment
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9620> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B98A0>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B98A0>
        Welcome to f with 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B98A0> TO <definition.ksinterpreter.Environment instance at 0x020B98A0>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B98A0> TO <definition.ksinterpreter.Environment instance at 0x020B98A0>
        x is too small, returning 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B98A0> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B98A0> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
      b is  3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
      a is  10  and b is  3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B9580>
      result is  13
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
    a is  26
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
    before we find b, let's check up on y. It is  1
Warning: evaluating identifier b. First assignment
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x020B9580> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9A80>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9A80>
      Welcome to f with 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9A80> TO <definition.ksinterpreter.Environment instance at 0x020B9A80>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9A80> TO <definition.ksinterpreter.Environment instance at 0x020B9A80>
      x is too small, returning 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9A80> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9A80> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
    b is  3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
    a is  26  and b is  3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B94B8>
    result is  29
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
  a is  58
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
  before we find b, let's check up on y. It is  1
Warning: evaluating identifier b. First assignment
CALLING SETENV. BY eval_exp ON f FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON f FROM <definition.ksinterpreter.Environment instance at 0x020B94B8> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B99B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B99B8>
    Welcome to f with 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B99B8> TO <definition.ksinterpreter.Environment instance at 0x020B99B8>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B99B8> TO <definition.ksinterpreter.Environment instance at 0x020B99B8>
    x is too small, returning 1
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B99B8> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B99B8> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
  b is  3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
  a is  58  and b is  3
CALLING SETENV. BY eval_exp ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
HEY! , CHANGING FUNC ENV OVER HERE. BY eval_element ON print FROM <definition.ksinterpreter.Environment instance at 0x020B9440> TO <definition.ksinterpreter.Environment instance at 0x020B9440>
  result is  61
61
