try:
 a= int(input("Enter a number:"))
 b= int(input ("Enter another number:"))
 print ("Result:",a/b)

except ValueError:
 print ("Use numbers only")

except ZeroDivisionError:
 print ("Can't divide by zero")

finally:
 print ("Execution Complete")