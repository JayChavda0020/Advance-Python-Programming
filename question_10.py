# Write a Python program to count the frequency of words in a file.
 
f = open("demo01.txt") 
 
d = dict() 

for line in f: 
	line = line.strip() 
	line = line.lower() 
	words = line.split(" ") 
					
	for word in words: 
		if word in d: 
			d[word] = d[word] + 1
		else:  
			d[word] = 1

for key in list(d.keys()): 
	print(key, ":", d[key])
	
f.close()
