arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

max_num = max(arr)
exp = 1  
while max_num // exp > 0:
    count = [0] * 10  
    output = [0] * len(arr)
    
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]
    
    exp *= 10

print("Sorted array:", arr)