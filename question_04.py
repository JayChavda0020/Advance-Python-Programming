# Write a Python program to read first n lines of a file. 

f = open("demo01.txt")

content = f.readlines()

print("first three line")
print(content[0:3])

f.close()