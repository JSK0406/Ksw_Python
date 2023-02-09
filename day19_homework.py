# 11-01

score_arr = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

def insert_sort(arr):
    n = len(score_arr)
    for right in range(n):
        for left in range(right, 0, -1):
            if score_arr[left][1] < score_arr[left-1][1]:
                score_arr[left], score_arr[left-1] = score_arr[left-1], score_arr[left]

    return arr

print('정렬 전 -->', score_arr)
print('정렬 후 -->', insert_sort(score_arr))
for i in range(len(score_arr)//2):
    print(score_arr[i][0], ':', score_arr[len(score_arr)-i-1][0])