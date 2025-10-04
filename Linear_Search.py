#Write a program to perform linear search on a list and print the index if found.

arr = [5, 10, 15, 20, 25]
key = 20
found  = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element Found at index:",i)
        found = True
        break

if not found:
    print("No Element Found")

print("Sorted Array:",arr)
