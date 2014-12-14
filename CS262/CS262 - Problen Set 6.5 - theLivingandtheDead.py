# The Living and the Dead

# In this assignment, you will write an optimizer that removes dead code. 
# For simplicity, we will only consider sequences of assignment statements
# (once we can optimize those, we could weave together a bigger optimizer
# that handles both branches of if statements, and so on, but we'll just do
# simple lists of assignments for now). 
#
# We will encode JavaScript fragments as lists of tuples. For example,
#
#               a = 1;
#               b = a + 1;
#               c = 2;
#
# Will be encoded as:
#
fragment2 = [ ("a", ["1"] ) ,           # a = 1
              ("b", ["a", "1"] ),       # b = a operation 1
              ("c", ["2"] ), ]          # c = 2 
# 
# Write a procedure removedead(fragment,returned). "fragment" is encoded
# as above. "returned" is a list of variables returned at the end of the
# fragment (and thus LIVE at the end of it). 
#

def removedead(fragment,returned):
        # fill in your answer here (can be done in about a dozen lines)
        optimized = []
        live = returned[:]
        for assignment in fragment[::-1] :
            if assignment[0] in live:  # this line is important, keep it
                optimized += [assignment]
                live = [var for var in live if var != assignment[0]]
            live += assignment[1]
        
        optimized = optimized[::-1]
        
        if fragment != optimized:    # recursiveness
            return removedead(optimized, returned)
        return optimized

# We have provided a few test cases. You may want to write your own.

fragment1 = [ ("a", ["1"]), 
              ("b", ["2"]), 
              ("c", ["3"]), 
              ("d", ["4"]), 
              ("a", ["5"]), 
              ("d", ["c","b"]), ]


print removedead(fragment1, ["a","d"])
print removedead(fragment1, ["a","d"]) == \
        [('b', ['2']), 
         ('c', ['3']), 
         ('a', ['5']), 
         ('d', ['c', 'b'])]

print removedead(fragment2, ["c"]) == [('c', ['2'])]

print removedead(fragment1, ["a"]) == [('a', ['5'])]

print removedead(fragment1, ["d"]) == \
        [('b', ['2']), 
         ('c', ['3']), 
         ('d', ['c', 'b'])]

