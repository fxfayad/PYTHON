arr = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter number to search: "))

left, right = 0, len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(f"Found at position {mid + 1}") 
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Not found")