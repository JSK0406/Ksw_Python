# 퀵정렬 구현

score_arr = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]


def quick_sort(arr, start, end):
    if end <= start:
        return
    pivot = arr[(start+end)//2][1]
    left = start
    right = end
    while left <= right:
        while arr[left][1] < pivot:
            left += 1
        while arr[right][1] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    quick_sort(arr, start, left-1)
    quick_sort(arr, left, end)
    return arr


print(quick_sort(score_arr, 0, len(score_arr)-1))