# Write a Python program to count the number of lines in a text file.

f = open("demo01.txt")
lines = len(f.readlines())
print(lines)

f.close()