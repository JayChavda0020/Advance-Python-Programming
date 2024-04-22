# Write a Python program to append text to a file and display the text

f =open("demo01.txt","a")
f .write("this is file management demo using python.\n")
f .close()
print("file  written succesfully")


f =open("demo01.txt","r")
print(f .read())
f .close()