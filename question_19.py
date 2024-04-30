# How Do You Handle Exceptions With Try/Except/Finally In Python ? Explain with coding snippets. 


def divide(x, y): 
	try: 
		result = x // y 
	except ZeroDivisionError: 
		print("Sorry ! You are dividing by zero ") 
	else:
		print("Yeah ! Your answer is :", result) 
	finally: 
		# this block is always executed 
		# regardless of exception generation. 
		print('This is always executed') 

# Look at parameters and note the working of Program 
divide(3, 2) 
divide(3, 0)
