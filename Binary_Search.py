# Write a program to perform binary search on a sorted array.

arr = [10, 20, 30, 40, 50]
key = 30
n =len(arr)
left =0
right =4
Found = False


while left <= right:
    mid = (left + right) //2

    if arr[mid] == key:
        print("Element found at index: ", mid)
        Found= True
        break

    elif arr[mid] < key:
        left = mid+1
    else:
        right = mid-1

if not Found:
    print("No Element Found")

print("Sorted Array:",arr)

