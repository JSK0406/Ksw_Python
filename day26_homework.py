import random


def seq_search(arr, find_data):
    for i in range(len(arr)):
        if arr[i] == find_data:
            return i+1


def bin_search(arr, find_data):
    left = 0
    right = len(arr) - 1
    cnt = 0
    while left <= right:
        cnt += 1
        mid = (left + right) // 2
        if arr[mid] == find_data:
            break
        elif arr[mid] < find_data:
            left = mid + 1
        else:
            right = mid - 1
    return cnt


find_data = 7878

data_arr = [random.randint(0, 999999) for _ in range(1000000)]
data_arr.insert(random.randint(0, 1000000), find_data)
sorted_arr = sorted(data_arr)

print('#비정렬 배열(100만개) -->', data_arr[0:5], '~~~~', data_arr[-5:len(data_arr)])
print('#정렬 배열(100만개) -->', sorted_arr[0:5], '~~~~', sorted_arr[-5:len(sorted_arr)])

print('순차 검색(비정렬 데이터) -->', seq_search(data_arr, find_data), '회')
print('순차 검색(비정렬 데이터) -->', bin_search(data_arr, find_data), '회')
