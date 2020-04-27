##################  If Elif and Else with User Input ##################################

a = int(input("Enter Number between 1 to 5 : "))
b = int(input("Enter Number between 6 to 14 : "))
c = int(input("Enter Number between 20 to 30 : "))

if(a>c):
    print("A is Smaller than C") # False 
elif(b>c):
    print("B is Smaller than C ") # False
elif(c<a):        
    print("A is Greater than C ") # False
elif(b<a):
    print("B is Smaller than A ") # False 
else:
    print("C is Greter than All element ") 
           