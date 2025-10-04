# Write a program to sort an array of floating-point numbers using Bucket Sort.

def BucketSort(arr):
    n= len(arr)
    buckets = [[] for i in range(n)]

    for num in arr:
        index = int(n* num)
        buckets[index].append(num)

    for i in range(n):
        buckets[i].sort()

    sort_arr =[]
    for bucket in buckets:
        sort_arr.extend(bucket)

    return  sort_arr



arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

print("Original Array", arr)
arr= BucketSort(arr)
print("Sorted Array", arr)