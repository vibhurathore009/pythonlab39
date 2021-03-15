c = input("enter character")
if c>='a' and c <= 'z':
    print("lowercase")
elif c>='A' and c <='Z':
    print("uppercase")
elif c>='0' and c <='9':
    print("digits")
else:
    print("special character")
