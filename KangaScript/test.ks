#print ([1,2,3][::])
#
#for i in [1,2,3,4,5]:
#	print(i)
#endfor
#
#if false:
#	print("Hello, World!")
#elif true:
#	print("What's up")
#otherwise:
#	print("Goodbye, World!")
#endif

#print( [i for i in ["a","b","c","d"]] )

for i in [i for i in range(10)]:
	# skip odd numbers
	if i%2==1:
		continue
	
	# don't go after 9
	# just to show off break statement
	elif i>9:
		break
	
	otherwise:
		print(i)
	endif
endfor

# What is 2 + 3 * 4?
# should be 14
# could return 20 if precedence is incorrect
print(2 + 3 * 4)	# 14 -- 14
print(4 * 3 + 2)	# 14 -- 20
print(2 + 4 * 3)	# 14 -- 14
print(3 * 4 + 2)	# 14 -- 18



	# operator precedence is not quite correct yet,
	# so 1==i%2 has to be in that order
	# i%2==1 would group like i%(2==1)
	# ... for some odd reason
