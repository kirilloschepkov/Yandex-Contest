from typing import Any


def push(elem, stack) -> str:
    stack.append(elem)
    return 'ok'


def pop(stack) -> Any:
    if size(stack):
        return stack.pop()
    return 'error'


def back(stack) -> Any:
    if size(stack):
        return stack[-1]
    return 'error'


def size(stack) -> int:
    return len(stack)


def clear(stack) -> str:
    stack.clear()
    return 'ok'


st = list()
while True:
    res, command = 0, (input() + ' plg').split()
    if command[0] == 'push': res = push(command[1], st)
    elif command[0] == 'pop': res = pop(st)
    elif command[0] == 'back': res = back(st)
    elif command[0] == 'size': res = size(st)
    elif command[0] == 'clear': res = clear(st)
    else:
        print('bye')
        break
    print(res)
