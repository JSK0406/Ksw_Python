import tkinter as tk


# def recur(n):
#     return n if n <= 1 else recur(n - 2) + recur(n - 1)
#
#
# def iter(n):
#     first = 0
#     second = 1
#     if n == 0:
#         return first
#     elif n == 1:
#         return second
#     for i in range(n-1):
#         tmp = first + second
#         first, second = second, tmp
#     return second
#
#
dp = [0] * 50
dp[0] = 0
dp[1] = 1

def memo(n):
    global dp
    if n >= 2:
        for i in range(n-1):
            dp[i+2] = dp[i+1] + dp[i]
    return dp[n]

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
#
#
# def memo_recur(n):
#
# print(recur(10))
# print(iter(10))
# print(memo(40))


win = tk.Tk()
win.title("Caculator")
win.geometry("250x150")


def fact_entry_input():
    lbl_result.config(text=f"계산기 출력 결과 : {fact(int(en_num_input.get()))}")


def fibo_entry_input():
    lbl_result.config(text=f"계산기 출력 결과 : {memo(int(en_num_input.get()))}")

en_num_input = tk.Entry()
lbl_result = tk.Label(text="계산기 출력 결과 : ")
btn_fact = tk.Button(text="팩토리얼", command=fact_entry_input)
btn_fibo = tk.Button(text="피보나치", command=fibo_entry_input)

en_num_input.pack()
lbl_result.pack()
btn_fact.pack(fill='x')
btn_fibo.pack(fill='x')

win.mainloop()

