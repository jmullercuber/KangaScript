grid=[]
for i in range(50):
	if i == 9 or i == 10 or i == 12 or i == 13:
		grid += [1]
	otherwise:
		grid += [0]
	endif
endfor

#.....................................................
sz = x = timeset = 0		# drawGrid
xin = neighborself = blank	# testSpot
NewGrid = blank				# next
acceptedArray = [1, 4, 7]
#.....................................................


function drawGrid():
	# no code to reset the screen
	# continuous flow
	
	result = ""
	for data in grid:
		if data == 1:
			result += "X"
		otherwise:
			result += " "
		endif
	endfor
	
	print(result)
	timeset += 1
endfunction


function next():
	NewGrid = []
	for sx in range(50):
		
		
		nebnumb = 0
		
		
		# testSpot
		p = -1
		while p < 2:
			if (sx + p < 0):
				xin = 50 - 1
			elif (sx + p > 50 - 1):
				xin = 0
			otherwise:
				xin = sx + p
			endif
			print(xin)
			print(grid[xin])
			neighbor = (grid[xin])
			nebnumb += 2^(p+1)*neighbor
			p += 1
		endwhile
		
		
		
		# evaluate
		e = 0
		for a in acceptedArray:
			if (nebnumb == a):
				e = 1
				break
			endif
		endfor
		
		
		NewGrid += [e]
	endfor
	grid = NewGrid
endfunction


# main
function draw():
	#drawGrid()
	next()
endfunction

draw()
draw()
draw()
draw()
