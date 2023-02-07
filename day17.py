import webbrowser
import time

def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE - 1:
        return True
    return False


def is_stack_empty():
    global SIZE, stack, top
    if top <= -1:
        return True
    return False


def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is full")
        return
    top += 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        return
    tmp = stack[top]
    stack[top] = None
    top -= 1
    return tmp



def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is empty")
        return None
    return stack[top]

def check_bracket(expr) :
	for ch in expr:
		if ch in '([{<':
			push(ch)
		elif ch in ')]}>':
			out = pop()
			if ch == ')' and out == '(':
				pass
			elif ch == ']' and out == '[':
				pass
			elif ch == '}' and out == '{':
				pass
			elif ch == '>' and out == '<':
				pass
			else:
				return False
		else :
			pass
	return is_stack_empty()


if __name__ == "__main__" :
    # url 방문

    # top = -1
    # SIZE = 100
    # stack = [None] * SIZE
    # urls = [ 'inha.edu', 'harvard.edu', 'yale.edu']
    #
    # for url in urls :
    #     push(url)
    #     webbrowser.open('http://'+url)
    #     print(url, end = '-->')
    #     time.sleep(1)
    #
    # print("방문 종료")
    # time.sleep(5)
    #
    # while True :
    #     url = pop()
    #     if url == None :
    #         break
    #     webbrowser.open('http://'+url)
    #     print(url, end = '-->')
    #     time.sleep(1)
    # print("방문 종료")

    SIZE = 100
    stack = [None for _ in range(SIZE)]
    top = -1

    expr_arr = ['(2*[3+1)]', '(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']

    for expr in expr_arr:
        top = -1
        print(expr, '==>', check_bracket(expr))
