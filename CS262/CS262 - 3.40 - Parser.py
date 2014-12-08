grammar = [
	("exp", ["exp", "+", "exp"]),
	("exp", ["exp", "-", "exp"]),
	("exp", ["(", "exp", ")"]),
	("exp", ["num"]),
]

# Expanding Exp
# This is very, very difficult.


def expand(tokens, grammar):
    #for pos in range(len(tokens)):
        for rule in grammar:
            # hmmmm
            if rule[0] in tokens:
                for w in tokens:
                    yield ([w] if w!=rule[0] else rule[1][:])
            
            
depth = 1
utterances = [["exp"]]
for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [ i for i in expand(sentence, grammar)]

for sentence in utterances:
    print sentence
    
#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']
