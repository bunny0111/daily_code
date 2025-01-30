def right_angle_triangle(rows):
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print('*', end='')
        print()

right_angle_triangle(5)