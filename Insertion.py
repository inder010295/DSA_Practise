# Write a Python program to insert an element at a specific position in an array.
arr = [10, 20, 30, 40]
element = 25
position = 2

arr.append(0)
for i in range(len(arr)-1, position, -1):
    arr[i] =arr[i-1]
arr[position] = element
print("Sorted array", arr)

