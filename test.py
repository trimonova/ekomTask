initial_field = []
count_field = []
with open('input.txt') as f:
    all_lines = f.readlines()
    n, m, k = map(int, all_lines[0].split())
    print(n, m, k)
    print(all_lines)
    for n in range(1, len(all_lines)):
        initial_line = list(map(int, all_lines[n].split()))
        initial_field.append(initial_line)
        copy_line = [0 for i in initial_line]
        count_field.append(copy_line)
        print(initial_line)
        print(initial_field)

a = [5]
b = a
b[0] = 3
print(a, b)