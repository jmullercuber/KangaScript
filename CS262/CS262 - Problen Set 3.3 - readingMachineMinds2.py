# Reading Machine Minds 2
#
# We say that a finite state machine is "empty" if it accepts no strings.
# Similarly, we say that a context-free grammar is "empty" if it accepts no
# strings. In this problem, you will write a Python procedure to determine
# if a context-free grammar is empty.
#
# A context-free grammar is "empty" starting from a non-terminal symbol S 
# if there is no _finite_ sequence of rewrites starting from S that
# yield a sequence of terminals. 
#
# For example, the following grammar is empty:
#
# grammar1 = [ 
#       ("S", [ "P", "a" ] ),           # S -> P a
#       ("P", [ "S" ]) ,                # P -> S
#       ] 
#       
# Because although you can write S -> P a -> S a -> P a a -> ... that
# process never stops: there are no finite strings in the language of that
# grammar. 
#
# By contrast, this grammar is not empty: 
#
# grammar2 = [
#       ("S", ["P", "a" ]),             # S -> P a
#       ("S", ["Q", "b" ]),             # S -> Q b
#       ("P", ["P"]),                   # P -> P
#       ("Q", ["c", "d"]),              # Q -> c d 
#
# And ["c","d","b"] is a witness that demonstrates that it accepts a
# string.
#
# Write a procedure cfgempty(grammar,symbol,visited) that takes as input a
# grammar (encoded in Python) and a start symbol (a string). If the grammar
# is empty, it must return None (not the string "None", the value None). If
# the grammar is not empty, it must return a list of terminals
# corresponding to a string in the language of the grammar. (There may be
# many such strings: you can return any one you like.) 
#
# To avoid infinite loops, you should use the argument 'visited' (a list)
# to keep track of non-terminals you have already explored. 
#
# Hint 1: Conceptually, in grammar2 above, starting at S is not-empty with
# witness [X,"a"] if P is non-empty with witness X and is non-empty with
# witness [Y,"b"] if Q is non-empty with witness Y. 
#
# Hint 2: Recursion! A reasonable base case is that if your current
# symbol is a terminal (i.e., has no rewrite rules in the grammar), then
# it is non-empty with itself as a witness. 
#
# Hint 3: all([True,False,True]) = False
#         any([True,True,False]) = True

def cfgempty(grammar,symbol,visited):
    print symbol, visited
    # Base Case
    if symbol in visited:
        return None
    # create this super-duper list that i'll use twice
    applicable_rules = [rule for rule in grammar if rule[0] == symbol]
    # ... still Base Case..., if symbol is terminal
    if len(applicable_rules) == 0:
        return [symbol]
    # Apply all the rules we can
    for rule in applicable_rules:
        result = []
        for newSymbol in rule[1]:
            print "newSymbol", newSymbol
            sub_result = cfgempty(grammar, newSymbol, visited + [symbol])
            print "Sub_Result:", sub_result
            if sub_result == None:    # bad
                # Don't taint the result!
                break # then move on to next applicable rule
            else: # good
                result += sub_result # grow the result
                print "Current Result", result
        else:
            print "Return", result
            return result
    # If the above didn't get us anywhere
    return None
                    
# We have provided a few test cases for you. You will likely want to add
# more of your own. 

grammar1 = [ 
      ("S", [ "P", "a" ] ),           
      ("P", [ "S" ]) ,               
      ] 
                        
print cfgempty(grammar1,"S",[]) == None ,"\n", "-"*20

grammar2 = [
      ("S", ["P", "a" ]),             
      ("S", ["Q", "b" ]),             
      ("P", ["P"]), 
      ("Q", ["c", "d"]),              
      ] 

print cfgempty(grammar2,"S",[]) == ['c', 'd', 'b'] ,"\n", "-"*20


grammar3 = [  # some Spanish provinces
        ("S", [ "Barcelona", "P", "Huelva"]),
        ("S", [ "Q" ]),
        ("Q", [ "S" ]),
        ("P", [ "Las Palmas", "R", "Madrid"]),
        ("P", [ "T" ]),
        ("T", [ "T", "Toledo" ]),
        ("R", [ ]) ,
        ("R", [ "R"]), 
        ]

print cfgempty(grammar3,"S",[]) == ['Barcelona', 'Las Palmas', 'Madrid', 'Huelva'] ,"\n", "-"*20

