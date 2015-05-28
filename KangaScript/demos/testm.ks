# Thanks to the code at http://rosettacode.org/wiki/Sierpinski_triangle#Python
# off which this is based!

# sierpinski() returns an array representing the sierpinski triangle
# each element is a row of the graphic
# the triangle has n mini triangles
function sierpinski(n):
    d = ["*"]
    
    for i in range(n):
        sp = " " * (2^i)
        d = [sp+x+sp for x in d] + [x+" "+x for x in d]
    endfor
    #print("it's sierpinski", this)
    return d
    
endfunction


# print out all the rows now!
for l in sierpinski(4):
    print(l)
endfor

# print!
print("")
print("Hey Ms. McDonnell, it's KangaScript!")
print("")

