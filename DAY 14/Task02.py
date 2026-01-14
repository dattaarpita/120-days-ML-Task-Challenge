string="Nurses Run"
s=string.replace(" ","").lower() #string space will be removed, all string will lower
if s==s[::-1]: #reverse string
    print("Palindrome")
else:
    print("Not Palindrome")