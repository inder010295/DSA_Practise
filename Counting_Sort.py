#Write a program to sort an array using Counting Sort (non-negative integers only).

def CountingSort(arr):
    n= len(arr)
    k = max(arr)

    count = [0] * (k+1)

    for i in range(n):
        count[arr[i]] +=1

    index=0
    for i in range(k+1):
       while count[i] >0:
            arr[index] =i
            index +=1
            count[i] -=1
    return arr
arr = [4, 2, 2, 8, 3, 3, 1]
CountingSort(arr)
print("Sorted Array:", arr)



