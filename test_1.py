import copy
def create_field(i, j, neighbor_line, initial_field, count_field, new_field):
    if neighbor_line.count(2) >= 2:
        new_field[i][j] = 2
        if initial_field[i][j] != 2:
            count_field[i][j] += 1
    elif neighbor_line.count(2) >= 1 or neighbor_line.count(3) >= 1:
        new_field[i][j] = 3
        if initial_field[i][j] != 3:
            count_field[i][j] += 1
    else:
        new_field[i][j] = 1
        if initial_field[i][j] != 1:
            count_field[i][j] += 1
    return count_field, new_field

initial_field = []

with open('input.txt') as f:
    all_lines = f.readlines()
    n, m, k = map(int, all_lines[0].split())
    for n in range(1, len(all_lines)):
        initial_line = list(map(int, all_lines[n].split()))
        initial_field.append(initial_line)

count_field = [[0] * m for i in range(n)]
new_field = [[0] * m for i in range(n)]


if n > 1 and m > 1:
    for step in range(k):
        for i in range(n):
            for j in range(m):
                neighbor_line = []
                if i == 0 and j == 0:
                    neighbor_line.append(initial_field[i + 1][j])
                    neighbor_line.append(initial_field[i][j + 1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif i == 0 and j == m-1:
                    neighbor_line.append(initial_field[i + 1][j])
                    neighbor_line.append(initial_field[i][j - 1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif i == n-1 and j == m-1:
                    neighbor_line.append(initial_field[i - 1][j])
                    neighbor_line.append(initial_field[i][j - 1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif i == n-1 and j == 0:
                    neighbor_line.append(initial_field[i - 1][j])
                    neighbor_line.append(initial_field[i][j + 1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif i == 0:
                    neighbor_line.append(initial_field[i+1][j])
                    neighbor_line.append(initial_field[i][j-1])
                    neighbor_line.append(initial_field[i][j+1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif i == n-1:
                    neighbor_line.append(initial_field[i - 1][j])
                    neighbor_line.append(initial_field[i][j - 1])
                    neighbor_line.append(initial_field[i][j + 1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif j == 0:
                    neighbor_line.append(initial_field[i][j+1])
                    neighbor_line.append(initial_field[i-1][j])
                    neighbor_line.append(initial_field[i+1][j])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif j == m-1:
                    neighbor_line.append(initial_field[i][j-1])
                    neighbor_line.append(initial_field[i-1][j])
                    neighbor_line.append(initial_field[i+1][j])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                else:
                    neighbor_line.append(initial_field[i][j - 1])
                    neighbor_line.append(initial_field[i][j+1])
                    neighbor_line.append(initial_field[i + 1][j])
                    neighbor_line.append(initial_field[i - 1][j])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)



        initial_field = copy.deepcopy(new_field)
    for element in count_field:
        for mini_element in element:
            print(mini_element, end=' ')
        print()


elif n == 1 and m != 1:
    for step in range(k):
        for i in range(n):
            for j in range(m):
                neighbor_line = []
                if j == 0:
                    neighbor_line.append(initial_field[i][j+1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif j == m - 1:
                    neighbor_line.append(initial_field[i][j - 1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)
                else:
                    neighbor_line.append(initial_field[i][j - 1])
                    neighbor_line.append(initial_field[i][j+1])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)
        initial_field = copy.deepcopy(new_field)
    for element in count_field:
        for mini_element in element:
            print(mini_element, end=' ')
        print()

elif m == 1 and n != 1:
    for step in range(k):
        for i in range(n):
            for j in range(m):
                neighbor_line = []
                if i == 0:
                    neighbor_line.append(initial_field[i+1][j])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)

                elif i == n - 1:
                    neighbor_line.append(initial_field[i -1][j])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)
                else:
                    neighbor_line.append(initial_field[i-1][j])
                    neighbor_line.append(initial_field[i+1][j])
                    count_field, new_field = create_field(i, j, neighbor_line, initial_field, count_field, new_field)
        initial_field = copy.deepcopy(new_field)
    for element in count_field:
        for mini_element in element:
            print(mini_element, end=' ')
        print()


elif m == 1 and n == 1:
    if initial_field[0][0] != 1:
        print(1)
    else:
        print(0)








