function factorial(n):
	if n == 0:
		return 1
	otherwise:
		return n * (factorial(n - 1))
	endif
endfunction

# Print the factorials of the first 10 whole numbers
for i in range(10):
	print (factorial(i+1))
endfor
