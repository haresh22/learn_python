############### IF ad Else #######################
input("Name of Stdent : ")
input("Standard : ")
int(input("Enter your Roll No : "))

a = int(input("Enter the English Marks : "))
if (a>=35):
    print("You are Pass ")
else:
    print("You are Fail ")    
b = int(input("Enter The Maths Marks :"))
if (b>=35):
    print("You are Pass ")
else:
    print("You are Fail ")    
c = int(input("Enter the Maths Marks : "))
if c>=35:
    print("You are Pass")
else:
    print("You are Fail ")

print("Total Marks =",300//a+b+c*100)
