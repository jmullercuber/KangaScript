function derive(f):
    fprime = []
    
    for e in f:
        de = [e[]e[2]-1]
        fprime += de
    endfor
    
    return fprime
endfunction

fp = derive( [ [1, 'x', 2], [4, 'x', 3], [5, 'x', 7], ] )

print( fp )
