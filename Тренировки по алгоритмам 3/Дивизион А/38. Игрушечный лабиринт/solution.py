def f(maze: list) -> int:
    for i in range(len(maze)):
        maze[i] = [1] + maze[i] + [1]
    maze.insert(0, [1] * len(maze[0]))
    maze.append([1] * len(maze[0]))
    length = [[-1] * len(maze[0]) for _ in range(len(maze))]
    length[1][1] = 0
    lst = list()
    lst.append((1, 1))
    while lst:
        x, y = lst.pop(0)
        if maze[x][y] == 2:
            return length[x][y]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i * i + j * j == 1:
                    cur_x, cur_y = x, y
                    while True:
                        if maze[cur_x][cur_y] == 2 or maze[cur_x + i][cur_y + j] == 1:
                            break
                        cur_x += i
                        cur_y += j
                    if length[cur_x][cur_y] == -1:
                        length[cur_x][cur_y] = length[x][y] + 1
                        lst.append((cur_x, cur_y))


print(f([list(map(int, input().split())) for _ in range(int(input().split()[0]))]))
