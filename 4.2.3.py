############## If Elif User Input ################

a = int(input("Enter number between 1 to 5 : "))
b = int(input("Enter number between 6 to 10 : "))
c = int(input("Enter number between 11 to 15 : "))

if(a>b):
    print("A is Smaller than B ") # False 
elif(b>c):
    print("B is Greater than C ") #False
elif(a==b):
    print("A and B are Equal ? ") # False 
elif(a<c):
    print("C is Greater than A ") # True 
    