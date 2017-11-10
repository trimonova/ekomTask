n, m, k = map(int, input().split())
initial_list = [[(1, 1/(n*m))],[(2, (n*m-1)/(n*m))]]
if n == 1 and m == 1 and k >= 1:
    print(1)

elif k == 2:
    print(1/(n*m) + 2 * (n*m-1)/(n*m))

else:
    old_list = initial_list * 2

    for shot in range(2, k):

        new_list_1 = []
        for element in old_list:
            new_element = element[:]
            new_list_1.append(new_element)
        new_list = new_list_1
        new_list.sort()

        for i in range(0, len(new_list), 2):
            shot_value = new_list[i][-1][0]
            if shot_value <= n*m:
                new_list[i].append((shot_value, shot_value/(n*m)))
                new_list[i + 1].append((shot_value + 1, (n * m - shot_value) / (n * m)))
            else:
                new_list[i].append((shot_value, 0))
                new_list[i+1].append((shot_value+1, 0))

        old_list = new_list*2

    mat = []
    for i in range(len(new_list)):
        mult = 1
        for j in new_list[i]:
            mult = mult * j[1]
        mat.append(mult*j[0])
    print(sum(mat))

