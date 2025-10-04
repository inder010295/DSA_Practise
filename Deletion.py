#Write a program to delete a specific element from an array.

arr = [10, 20, 30, 40]
element = 30
position=2
for i in range(position, len(arr)-1):
    arr[i] = arr[i+1]
    arr.pop()
print("Sorted Array", arr)