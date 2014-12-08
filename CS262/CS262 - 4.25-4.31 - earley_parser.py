def addtochart(chart, index, state):
    if state in chart[index]:
        return False
    
    chart[index] += [state]
    return True


def closure (grammar, i, x, ab, cd, j):
    return [
        (rule[0], [], rule[1], i)
        for rule in grammar
        if cd!=[] and rule[0]==cd[0]
    ]


def shift (tokens, i, x, ab, cd, j):
    #if i >= len(tokens) or cd[0] != tokens[i]:
    if cd == [] or cd[0] != tokens[i]:
        return None
    return (x, ab+[cd[0]], cd[1:], j)


def reductions(chart, i, x, ab, cd, j):
    if cd != []:
        return []
    return [
        (state[0], state[1]+[x], state[2][1:], state[3])
        for state in chart[j]
        if state[2] != [] and state[2][0] == x
    ]


def print_state(s):
    r = s[0] + ' --> '
    for e in s[1]:
        r += e
    r += ' . '
    for e in s[2]:
        r += e
    r +=  ' from ' + str(s[3])
    print r


grammar = [
    ( "S", ["P"] ),				# S --> P
    ( "P", ["(", "P",")"] ),	# P --> ( P )
    ( "P", [] ),				# P --> 
]
tokens = ["(", "(", ")", ")"]


def parse(tokens, grammar):
    tokens += ['end_of_input_marker']		# "padding", to make sure we don't run out of stuff
    chart = {}
    start_rule = grammar[0]					# by convention
    for i in xrange(len(tokens)+1):
    	chart[i] = []		# well-defined list, already full
    start_state = (start_rule[0], [], start_rule[1], 0)
    chart[0] = [ start_state ]		# initially, only thing true
    for i in xrange(len(tokens)):
        while True:
            changes = False			# apply the 3 rules (closure, shift, reduction), until done
            for state in chart[i]:
                # State ===   x --> ab . cd from j
                # extract those
                x, ab, cd, j = state
                
                
                # Current State ==  x --> ab . cd, j
                # Option 1: For each grammar rule	c -> p q r
                # (where the c's match)
                # make a next state					c -> . p q r, i
                # English: We're about to state parsing a "c", but
                # c may be something like "exp" with its own
                # production rules. We'll bring those production rules in.
                next_states = closure(grammar, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes
                
                
                # Current State ==  x --> ab . cd, j
                # Option 2: If tokens[i] == c
                # make a next state					x --> abc . d, j
                # in chart[i+1]
                # English: We're looking for to parse token c next
                #  and the current token is exactly c! Aren't we lucky!
                #  So we can parse over it and move to j+1
                next_state = shift(tokens, i, x, ab, cd, j)
                if next_state != None:
                    changes = addtochart(chart, i+1, next_state) or changes
                
                
                # Current State ==  x --> ab . cd, j
                # Option 3: If cd is [], the state is just x --> ab . , j
                # for each p -> q . x r, l in chart[j]
                # make a next state					p --> qx . r, l
                # in chart[i]
                # English: We just finished parsing an "x" with this token,
                #  but that may have been a sub-step (like maching "exp --> 2"
                #  in "2+3"). We should update the higher-level rules as well.
                next_states = reductions(chart, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes
                
            # end for loop, looking at every state
            
            # We're done if nothing changed!
            if not changes:
                break
                
        # end While True loop, to parse current token
    # end for loop to look at every token
    
    for i in xrange(len(tokens)): # print out the chart, debugging stuff
        print "== chart", i
        for state in chart[i]:
            print_state(state)
    # end for loop debugging
    
    accepting_state = (start_rule[0], start_rule[1], [], 0)
    return accepting_state in chart[len(tokens)-1]		# this is it! we parsed it !!!!!!
    
# end function parse()
import sys
if len(sys.argv) == 2:
    print parse([c for c in sys.argv[1]], grammar)
else:
    print parse(tokens, grammar)
quit()

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ("t",["I","like","t"]),
    ("t",[""])
    ]


states1 = [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",["exp","+"],["exp"]) == states1
print closure(grammar,0,"exp",[],["exp","+","exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",["exp"],["+","exp"]) == []



print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0) == ('exp', ['exp', '+', 'exp'], [], 0)
print shift(["exp","+","exp"],0,"exp",[],["exp","+","exp"],0) == ('exp', ['exp'], ['+', 'exp'], 0)
print shift(["exp","+","exp"],3,"exp",["exp","+","exp"],[],0) == None
print shift(["exp","+","ANDY LOVES COOKIES"],2,"exp",["exp","+"],["exp"],0) == None


chart = {0: [('exp', ['exp'], ['+', 'exp'], 0), ('exp', [], ['num'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['exp', '+', 'exp'], 0)], 1: [('exp', ['exp', '+'], ['exp'], 0)], 2: [('exp', ['exp', '+', 'exp'], [], 0)]}

print reductions(chart,2,'exp',['exp','+','exp'],[],0) == [('exp', ['exp'], ['-', 'exp'], 0), ('exp', ['exp'], ['+', 'exp'], 0)]
