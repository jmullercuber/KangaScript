# Based off of jmullercuber's (that's mine) program on Khan Academy
# http://www.khanacademy.org/computer-programming/1-dimensional-cellular-automaton/1429069204
###
# * Hello,
# * This is a simulation of a cellular automaton, in 1 dimension. (Okay, 2 if you count time)
# * Each cell is in either a ON or OFF state. Or, if you prefer, it could be (1/0), (BLACK/WHITE), (HUNGRY/FULL). It doesn't matter.
# * The cells exist in a 1D line, represented by a single row on the screen. In each time-step, the cells react to one another, altering their states. The new set of cells is then pasted below in the terminal. (This is what I mean by a second dimension for time).
# * Also, just how the 2D Game of Life takes on a torus, this automaton is on a circle. That is, cells on the far left and right can interact with each other. Explaination of this idea on Wikipedia link.
# * 
# * Variables you are welcome to change are:
# *  dimension - How many cells?
# *  acceptedArray - Rules the cells follow. Explained at bottom
# *  inital values - use the plotter function
# * 
# * Check these out for more:
# *      http://en.wikipedia.org/wiki/Cellular_automaton#Overview
# *      http://en.wikipedia.org/wiki/Elementary_cellular_automaton
# * 
###....................................................
dimension = 50

grid = [ 0 for i in range(dimension) ]

acceptedArray = [1, 4, 7]
#......................................................
function ploter(xt, state):
    grid[xt] = state
endfunction

# Inital values
ploter (9, 1)
ploter (10, 1)
ploter (12, 1)
ploter (13, 1)

function drawGrid(grid):
    s = ""
    for cell in grid:
        if cell:
            s += '#'
        otherwise:
            s += ' '
        endif
    endfor
    print(s)
endfunction

function uniquelyIdentifyed(nebArray):
    nebnumb = 0
    for i in range(3):
        nebnumb += (2^i) * nebArray[i]
    endfor
    return nebnumb
endfunction

function testSpot(sx, grid, acceptedArray):
    neighborself = [0,0,0]
    for p in [-1, 0, 1]:
        if sx+p < 0:
            xin = dimension - 1
        elif sx+p > dimension-1:
            xin = 0
        otherwise:
            xin = sx + p
        endif
        neighborself[p+1] = grid[xin]
    endfor
    return uniquelyIdentifyed(neighborself) in acceptedArray
endfunction

function draw():
    drawGrid(grid)
    grid = [
        testSpot(xu, grid, acceptedArray)
        for xu in range(dimension)
    ]
endfunction

# Demonstrate Infinitely!
while true:
    draw()
endwhile

#```````````````````````Accepted States`````````````````````````````
###
# *  #       Left-Middle-Right States
# *  0       000
# *  1       100
# *  2       010
# *  3       110
# *  4       001
# *  5       101
# *  6       011
# *  7       111
###
