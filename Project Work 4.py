print("Welcome to the Data Analyzer and Transformer Program\n")
array = []
def fact(n):
    if n <=1:
        return 1
    else:
        return n *fact(n-1)
def statistics(arr):
    minimum = min(arr)
    maximum = max(arr)
    addition = sum(arr)
    avg = sum(arr)/ len(arr)
    return minimum, maximum, addition, addition, avg
is_on = True
while is_on:
    choice = int(input("Main Menu: \n1. Input Data\n2. Display Data Summary (Built-in Functions)\n3. Calculate Factorial (Recursion)\n4. Filter Data by Threshold (Lambda Functions)\n5. Sort Data\n6. Display Dataset Statistics (Return Multiple Values)\n7. Exit Program\nPlease enter your choice:  "))
    if choice == 1:
        n = int(input("Enter how many elements: "))
        for i in range(n):
            array.append(int(input("Enter elem: ")))
        print("Data has been stored successfully!")
    elif choice == 2:
        print(f"Data Summary: ")
        print(f"Total elements: {len(array)}")
        print(f"Minimum value: {min(array)}")
        print(f"Maximum value: {max(array)}")
        print(f"Sum of all values: {sum(array)}")
        print(f"Average value: {sum(array)/len(array)}")
    elif choice == 3:
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"Factorial of {num} is: {fact(num)}")
    elif choice == 4:
        value = int(input("Enter a threshold value to filter out data below this value: "))
        filtered_data = lambda val: [i for i in array if 1>val]
        print(f"Factorial Data (values >= {value}): {filtered_data(value)}")
    elif choice == 5:
        print("Choose sorting option: ")
        print("1. Ascending")
        print("2. Decending")
        order = int(input("Enter your choice: "))
        if order == 1:
            print(f"Sorted Data in {order} order: ")
    elif choice == 6:
        pass
    elif choice == 7:
        print("\nThankyou for using the Data Analyzer and Transformer Program. Goodbye!")
        is_on = False
    else:
        print("INVALID CHOICE!")
        is_on = False