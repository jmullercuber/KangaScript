function F(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	otherwise:
		return F(n-1) + F(n-2)
	endif
endfunction

for i in range(10):
	print ( F(i) )
endfor
