# Write a program to sort an array using Selection Sort.

arr = [64, 25, 12, 22, 11]

n= len(arr)

for i in range(n-1):
    minIndex=i

    for j in range(i+1,n):
        if arr[j] < arr[minIndex]:
            minIndex =j
    arr[i], arr[minIndex] = arr[minIndex], arr[i]

print("Sorted Array", arr)



