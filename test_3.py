import copy
import sys
n, m, k = map(int, input().split())
initial_list = [[(1, 1/(n*m))],[(2, (n*m-1)/(n*m))]]
old_list = initial_list * 2

#print(new_list)

for shot in range(2, k):

    new_list_1 = []
    for element in old_list:
        new_element = element[:]
        new_list_1.append(new_element)
    new_list = new_list_1
    new_list.sort()

    for i in range(0, len(new_list), 2):
        shot_value = new_list[i][-1][0]
        print(shot_value)
        new_list[i].append((shot_value, shot_value/(n*m)))
        print(new_list[i] is new_list[i+1])
        new_list[i+1].append((shot_value+1, (n*m-shot_value)/(n*m)))
    old_list = new_list*2

print(new_list)
mat = []
for i in range(len(new_list)):
    mult = 1
    for j in new_list[i]:
        print(j)
        mult = mult * j[0]*j[1]
        print(mult)
    mat.append(mult)
print(sum(mat))

print(new_list)


