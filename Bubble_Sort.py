#Write a program to sort an array using Bubble Sort.

arr = [5, 1, 4, 2, 8]

n= len(arr)

for i in range(n-1):
    swapped = False

    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True

    if not swapped:
        break

print(arr)