#function tea(t):
#	for i in range(t):
#		print("t")
#	endfor
#endfunction
#
#print(range(3))
#print(tea(4))

function rec(r):
	print(r)
	if r:
		rec(r)
	endif
endfunction

rec(0)


# Functions inside of functions

function fungen(hello):
	return function (name):
		print(hello)
		print(name)
	endfunction
endfunction

print(fungen("Hello")("Charles the Hammer"))

function heyCharlie(hello):
	hello("Hey")("Charlie")
	print( hello("Hey")("Charlie") )	# strange error here
endfunction

heyCharlie(fungen)

