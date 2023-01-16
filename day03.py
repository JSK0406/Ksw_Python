start = int(input('start number : '))
end = int(input('end number : '))

if end < start:
    start, end = end, start

for num in range(start, end+1):
    if not num >= 2:
        continue
    for j in range(2, num):
        if num % j == 0:
            break
    else:
        print(num, end=' ')

print('')

while start <= end:
    i = 2
    while i <= start-1:
        if start % i == 0:
            break
        i += 1
    else:
        if start >= 2:
            print(start, end=' ')
    start += 1
