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

print( f(1) )
print( f(2) )
print( f(3) )
print( f(4) )
print( f(5) )
