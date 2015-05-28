# Author: Sam Goldman
# Purpose: isPrime is a primality test for integer n.
#   It uses the trial division algorithm
#   findPrimes prints out the first num primes
#   When run, the whole program finds the first 10 primes

function isPrime(n):
	### Ammended by Joey Muller ###
	# 1 and below are not prime
	if n < 2:
	  return false
	endif
	### End Ammend ###
	count = 0
	for i in range(n):
		a = n%(i + 1)
		if(a == 0):
			count = count + 1
		endif
	endfor
	
	if(count > 2):
		return false
	endif
	return true
endfunction

function findPrimes(num):
	count = 0
	i = 0
	while(count < num):
		i = i + 1
		c = isPrime(i)
		if(c == true):
			print(i)
			count+=1
		endif
	endwhile
endfunction

findPrimes(10)
