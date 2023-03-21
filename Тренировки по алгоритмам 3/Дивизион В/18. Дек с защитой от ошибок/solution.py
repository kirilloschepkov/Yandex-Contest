from typing import Any


def push_front(elem, q) -> str:
    q.insert(0, elem)
    return 'ok'


def push_back(elem, q) -> str:
    q.append(elem)
    return 'ok'


def pop_front(q) -> Any:
    if size(q):
        return q.pop(0)
    return 'error'


def pop_back(q) -> Any:
    if size(q):
        return q.pop()
    return 'error'


def front(q) -> Any:
    if size(q):
        return q[0]
    return 'error'


def back(q) -> Any:
    if size(q):
        return q[-1]
    return 'error'


def size(q) -> int:
    return len(q)


def clear(q) -> str:
    q.clear()
    return 'ok'


queue = list()
while True:
    res, command = 0, (input() + ' plg').split()
    if command[0] == 'push_front': res = push_front(command[1], queue)
    elif command[0] == 'push_back': res = push_back(command[1], queue)
    elif command[0] == 'pop_front': res = pop_front(queue)
    elif command[0] == 'pop_back': res = pop_back(queue)
    elif command[0] == 'front': res = front(queue)
    elif command[0] == 'back': res = back(queue)
    elif command[0] == 'size': res = size(queue)
    elif command[0] == 'clear': res = clear(queue)
    else:
        print('bye')
        break
    print(res)
