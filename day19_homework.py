# 10-01

num_char_lst = [chr((ord('0') + i)) for i in range(10)]
num_char_lst += [chr(65+i) for i in range(6)]

def notation(n, base):
    if n < base:
        print(num_char_lst[n], end='')
        return
    notation(n // base, base)
    print(num_char_lst[n % base], end='')

n = int(input('10진수 입력 --> '))
print('')

print('2진수 : ', end='')
notation(n, 2)
print('')
print('8진수 : ', end='')
notation(n, 8)
print('')
print('16진수 : ', end='')
notation(n, 16)
