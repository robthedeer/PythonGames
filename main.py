hash = 2
for x in range(2): 
    for x in range(1):
        print("#####################################")

print("\t\tWelkome\t\t")

for x in range(2): 
    for x in range(1):######
        print("#####################################")


#CHOICE
choice = int(input("CHOICE a number:(1-4)\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))

a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a/b

if choice==1:
  print("Addition is :",a+b)
elif choice==2:
  print("Subtraction is :",a-b)
elif choice==3:
  print("Multiplication is :",a*b)
elif choice==4:
  print("Division is :",a/b)
else:
  print("Wrong choice Entered!")