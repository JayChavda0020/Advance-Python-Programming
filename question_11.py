# Write a Python program to write a list to a file

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

f = open("demo01.txt", "w")
for c in color:
     f.write("%s\n" % c)

content = open('demo01.txt')
print(content.read())

f.close()
