function factorial(n):
	if n == 0:
		return 1
	otherwise:
		return n * (factorial(n - 1))
	endif
endfunction

for i in range(10):
	print (factorial(i))
endfor
