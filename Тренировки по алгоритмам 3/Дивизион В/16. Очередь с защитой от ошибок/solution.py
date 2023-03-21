from typing import Any


def push(elem, q) -> str:
    q.append(elem)
    return 'ok'


def pop(q) -> Any:
    if size(q):
        return q.pop(0)
    return 'error'


def front(q) -> Any:
    if size(q):
        return q[0]
    return 'error'


def size(q) -> int:
    return len(q)


def clear(q) -> str:
    q.clear()
    return 'ok'


queue = list()
while True:
    res, command = 0, (input() + ' plg').split()
    if command[0] == 'push': res = push(command[1], queue)
    elif command[0] == 'pop': res = pop(queue)
    elif command[0] == 'front': res = front(queue)
    elif command[0] == 'size': res = size(queue)
    elif command[0] == 'clear': res = clear(queue)
    else:
        print('bye')
        break
    print(res)


