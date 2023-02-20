import random

def binary_search(arr, find_product):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == find_product:
            return mid
        elif arr[mid] < find_product:
            left = mid + 1
        else:
            right = mid -1
    return -1



data_arr = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_arr = [random.choice(data_arr) for _ in range(20)]

print('#오늘 판매된 전체 물건(중복O, 정렬X) -->', sell_arr)
sell_arr.sort()
print('#오늘 판매된 전체 물건(중복O, 정렬O) -->', sell_arr)
sell_product = list(set(sell_arr))
print('#오늘 판매된 물품 종류(중복x) -->', sell_product)

count_lst = []

for product in sell_product:
    cnt = 0
    while True:
        product_idx = binary_search(sell_arr, product)
        if product_idx == -1:
            break
        else:
            del sell_arr[product_idx]
            cnt += 1
    count_lst.append((product, cnt))
print(count_lst)

print()
print("결산 결과 ==>", count_lst)
