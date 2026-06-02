print("Welcome to the first project of my course AI/ML Data science \n")

name = input("Enter your name : ")
age = int(input("Enter your age : "))
height = float(input("Enter your height in meters : "))
num = int(input("Enter your favourite number : "))

print("\nThank you giving me your details , the information we collected is : \n")
print("Name is : ",name,"Data type is :",type(name),"Memory Address is : ",id(name))
print("Age is : ",age,"Data type is :",type(age),"Memory Address is : ",id(age))
print("Height is : ",height,"Data type is :",type(height),"Memory Address is : ",id(height))
print("Favourite Number is : ",num,"Data type is :",type(num),"Memory Address is : ",id(num))


byear = 2026-age
print("\nYour Birthyear is approxemetley : ",byear,"\n")

print("Thank you for using the personal data collector . Have a good day !")