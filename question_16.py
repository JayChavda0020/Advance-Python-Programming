# Can one block of except statements handle multiple exception? 

# yes

try:
    n = int(input("Input a number: "))
    result = 10 / n
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero occurred.")
