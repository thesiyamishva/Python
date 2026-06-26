print("*****Welcome to the data anlayzer and transformer program***** ")

li = []

def take_input():
    global li
    li=[int(i) for i in input("\nEnter element sep by space:\n").split(" ")]
    print("\nElement inserted successfully !\n")
    
def Display_summary(li):
    print("\nData Summary:")
    print("Total elements:", len(li))
    print("Minimum value:",min(li)) 
    print("Maximum:",max(li))
    print("Sum of all values:",sum(li))
    print("Average values:", round(sum(li)/len(li),2))
    
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

def filter_data(li):
    value = int(input("Enter a threshold value to filter out data above this value:"))
    result = list(filter(lambda x: x > value,li))
    print("filtered Data:", result)
    
def sort_data(li):
    print("\n1. Ascending")
    print("2. Descending")
    
    choice = int(input("Enter your choice:"))
    
    if choice==1:
        sorted_list = sorted(li)
        
    elif choice==2:
        sorted_list = sorted(li,reverse=True)
        
    else:
        print("Invalid Choice")
        return
    print("Sorted List:", sorted_list)
    
def statistics(li):
    total = sum(li)
    avg = total / len(li)
    maximum = max(li)
    minimum = min(li)
    
    return total, avg, maximum, minimum
    
while True:
    
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions) ")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    
    choice = int(input("\nplease enter your choice: " ))
    
    if choice==1:
        take_input()
        
    elif choice==2:
        Display_summary(li)  
        
    elif choice==3:
        n= int(input("Enter number to calculate it's factorial: ")) 
        print("Factorial of number is : ", factorial(n))
        
    elif choice==4:
        filter_data(li) 
        
    elif choice==5:
        sort_data(li)
        
    elif choice==6:
        total, avg, maximum, minimum = statistics(li)
        print("Total:", total)
        print("Average:", avg)
        print("Maximum:", maximum)
        print("Minimum:", minimum)
        
    elif choice==7:
        print("Thank you for using the data analyzer and transformer program. Good bye!")
        break
    
    else:
        print("Invalid choice")
        