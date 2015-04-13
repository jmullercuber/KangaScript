# Author: Sam Goldman
# Purpose: Recursive implementation of integer exponentiation.
# Note: Mostly proof of concept. Exponentiation binary operator (**) is prefered

function exp(base, power):
	if(power == 0):
		return 1
	endif
	return exp(base, power - 1) * base
endfunction

print(exp(2,0))
print(exp(2,1))
print(exp(2,2))
print(exp(2,3))
print(exp(2,4))
print(exp(2,5))
print(exp(2,6))
print(exp(2,7))
print(exp(2,8))
#print(exp(2,9))

