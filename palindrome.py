string = input("Enter a string: ")
if string.lower() == string.lower()[::-1].lower():
    print(f"'{string}' string is a palindrome.")
else:
    print(f"'{string}' string is not a palindrome.")