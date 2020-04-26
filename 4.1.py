############### Logical "AND and EXPRESSION" ########################

a = int(input("Enter number between 1 to 10 : "))
b = int(input("Enter number between 11 to 20 : ")) 
c = int(input("Enetr number between 21 to 30 : "))
d = 1000
e = 2000

print(a<b and b>a)
print(b>a and b<c)
print(c>b and c>a)
print(c>a and d and e)
print(c<a and d)
print(c<a and d and e)