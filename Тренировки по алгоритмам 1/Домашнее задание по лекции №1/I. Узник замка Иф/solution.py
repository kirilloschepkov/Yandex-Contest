def f(x_brick, y_brick, z_brick, x_hole, y_hole: int) -> str:
    min_x_brick, min_y_brick = sorted([x_brick, y_brick, z_brick])[:2]
    if min(x_hole, y_hole) >= min_x_brick and max(x_hole, y_hole) >= min_y_brick:
        return 'YES'
    return 'NO'


print(f(int(input()), int(input()), int(input()), int(input()), int(input())))
