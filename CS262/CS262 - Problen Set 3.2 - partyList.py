import this

# Bonus Practice: Subsets

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

def partyList(invited, attending=[]):
    #print invited, attending
    if len(invited) == 0:
        print attending
    else:
        #print "Going deeper"
        partyList(invited[1:], attending + invited[:1])
        partyList(invited[1:], attending)

# Test it
friends = ['Dog', 'Cat', 'Mouse', 'Buffalo']

partyList(friends)
