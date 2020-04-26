############ Logical "OR" Expression with user input ##############################

a = int(input("Enter number between 1 to 5 : "))
b = int(input("Enter number between 10 to 15 : "))
c = int(input("Enter number between 21 to 25 : "))
d = 100
e = 200
print(a<b or b>a)
print(b<c or c>b)
print(c>a or a<c)
print(a==b or b==c)
print(c>a or d or e)
print(a>c or d or e )



