function F(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	otherwise:
		return F(n-1) + F(n-2)
	endif
endfunction

# Print the first 10 numbers of the fibonacci sequence, beginning with 1, 1
for i in range(10):
	print ( F(i+1) )
endfor
