# 11-01

arr2 = [[55, 33, 250, 44], [88, 1, 67, 23], [199, 222, 38, 47], [155, 145, 20, 99]]
arr1 = []
for i in arr2:
    arr1 += i

def insert_sort(arr):
    n = len(arr)
    for right in range(n):
        for left in range(right, 0, -1):
            if arr[left] < arr[left-1]:
                arr[left], arr[left-1] = arr[left-1], arr[left]

    return arr

print('정렬 전 -->', arr1)
print('정렬 후 -->', insert_sort(arr1))
print('중앙값 -->', arr1[len(arr1)//2])