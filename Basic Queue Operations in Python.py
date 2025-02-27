queue = []  

while True:
    print("\nQueue Operations:")
    print("1. Enqueue (Add element)")
    print("2. Dequeue (Remove element)")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to add: ")
        queue.append(element)  
        print(f"{element} added to the queue.")

    elif choice == 2:
        if not queue:
            print("Queue is empty. Cannot dequeue.")
        else:
            removed_element = queue.pop(0)  
            print(f"Removed element: {removed_element}")

    elif choice == 3:
        if not queue:
            print("Queue is empty.")
        else:
            print("Current Queue:", queue)

    elif choice == 4:
        print("Exiting program.")
        break  

    else:
        print("Invalid choice! Please enter a valid option.")