while True:

    print("\n Welcome to the Pattern Generator and Number Analyzer! \n")

    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int (input("Enter Your Choice: "))

    match choice:
    
     case 1: 

          print("\n----- Pattern Menu -----")
          print("1. number Pattern")
          print("2. Pyramid Pattern")
          print("3. Dollar Triangle Pattern")
          print("4. star Pattern")
          
          choose = int(input("Enter pattern choice: "))

          match choose:

           case 1:
            rows = int(input("Enter the number of rows for the pattern: "))
    
            for i in range(1, rows + 1):
               print(str(i) * i)
    
           case 2:
             rows = int(input("Enter number of rows for the pattern: "))

             for i in range (1,rows + 1):
               print("^" *i)
         
           case 3:
             rows = int(input("Enter number of rows for the pattern: "))

             for i in range (1,rows + 1):
               print("$" *i)
                         
           case 4:
             rows = int(input("Enter number of rows: "))

             for i in range (1,rows + 1):
               print("*" *i)

           case _:
               print("Invalid Pattern Choice!")

     case 2:
         
          print("\nYou chose to Analyze a range of numbers\n")

          start = int(input("Enter the start of the range : "))
          end = int(input("Enter the end of the range : "))

          total = 0

          for i in range(start, end + 1):
                total += i

                if i % 2 == 0:
                    print("Number", i, "is even")
                else:
                    print("Number", i, "is odd")

          print("\nSum of all numbers from start to end is :", total)

     case 3:
         
          print("\nExiting the Program, Goodbye!")
          break

     case _:
         
          print("\nSorry! You entered an invalid choice!")
     
                        
                             
                        
    