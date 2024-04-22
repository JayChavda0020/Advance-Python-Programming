# Write a Python program to copy the contents of a file to another file. 

f1 = open("demo01.txt")
f2 = open("demo02.txt", "a")

for line in f1:
    f2.write(line)

f1.close()
f2.close()

f = open("demo02.txt")
print(f.read())
f.close()