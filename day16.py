# stack = [None]*5
# top = -1
#
# top += 1
# stack[top] = "커피"
# top += 1
# stack[top] = "녹차"
# top += 1
# stack[top] = "꿀물"
#
# for i in range(len(stack)-1, -1, -1):
#     print(stack[i])
#
# stack[top] = None
# top -= 1
# stack[top] = None
# top -= 1
#
# for i in range(len(stack) - 1, -1, -1):
#     print(stack[i])


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
        print("Stack is empty")
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


SIZE = int(input("Stack Size : "))
stack = [None] * SIZE
top = -1

if __name__ == "__main__":

    while True:
        select = input("Insert(I)/Extract(E)/Verify(V)/Exit(X) choose one ==> ")
        if select == 'X' or select == 'x':
            break
        elif select == 'I' or select == 'i':
            data = input("input data ==> ")
            push(data)
            print("스택 상태 : ", stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("extract data ==> ", data)
            print("status of stack : ", stack)
        elif select == 'V' or select == 'v':
            data = peek()
            print("verifyed data ==> ", data)
            print("status of stack : ", stack)
        else:
            print("input is wrong")

    print("Finish!")
