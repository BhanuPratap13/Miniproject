name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
aadhar=int(input("Enter your aadhar card number:"))
if(age>=18):
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")
if(age>=18):
    print("Choose the party you want to vote:")
    print('1. BJP')
    print('2. Congress')
    print('3. Shivsena')
    print('4. AAP')
    choice=int(input("Enter your choice:"))
    if(choice==1):
        print("You voted BJP")
        print("Thank You!")
    elif(choice==2):
        print("You voted Congress")
        print("Thank You!")
    elif(choice==3):
        print("You voted Shivsena")
        print("Thank You!")
    elif(choice==4):
        print("You voted AAP")
        print("Thank You!")
    else:
        print("You entered wrong input")