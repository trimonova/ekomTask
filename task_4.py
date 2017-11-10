with open('input.txt') as f:
    n = int(f.readline())

    all = f.readlines()
    all_list = []
    for line in all:

        all_list.append(list(map(int, line.split())))

if len(all_list) == 2:
    print('Yes')

else:
    beauty_obl = []
    not_beauty_obl = []
    for element in all_list:
        if element[2] == 1:
            beauty_obl.append(element)
        else:
            not_beauty_obl.append(element)

    if len(not_beauty_obl) > len(beauty_obl):
       beauty_obl, not_beauty_obl = not_beauty_obl, beauty_obl

    def rotate(A,B,C):
      return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

    def find_cover(A):
      n = len(A)
      P = list(range(n))
      for i in range(1,n):
        if A[P[i]][0]<A[P[0]][0]:
          P[i], P[0] = P[0], P[i]

      H = [P[0]]
      del P[0]
      P.append(H[0])

      while True:
          right = 0
          for i in range(1, len(P)):
              if rotate(A[H[-1]], A[P[right]], A[P[i]]) < 0:
                  right = i
          if P[right] == H[0]:
              break
          else:
              H.append(P[right])
              del P[right]
      return H
    beauty_cover = [beauty_obl[element] for element in find_cover(beauty_obl)]
    not_beauty_cover = [not_beauty_obl[element] for element in find_cover(not_beauty_obl)]

    for i in range(len(beauty_cover)):
        if i != len(beauty_cover)-1:
            new_center = beauty_cover[i]
            sin = (beauty_cover[i+1][1] - beauty_cover[i][1])/((beauty_cover[i+1][1] - beauty_cover[i][1])**2 + (beauty_cover[i+1][0] - beauty_cover[i][0])**2)**0.5
            cos = (beauty_cover[i+1][0] - beauty_cover[i][0])/((beauty_cover[i+1][1] - beauty_cover[i][1])**2 + (beauty_cover[i+1][0] - beauty_cover[i][0])**2)**0.5
            new1_nobeauty_obl = []
            new2_nobeauty_obl = []
            for point in not_beauty_obl:
                new1_nobeauty_obl.append([point[0]-new_center[0], point[1]-new_center[1]])
                new2_nobeauty_obl.append([new1_nobeauty_obl[-1][0]*cos + new1_nobeauty_obl[-1][1]*sin, -new1_nobeauty_obl[-1][0]*sin + new1_nobeauty_obl[-1][1]*cos])

        else:
            new_center = beauty_cover[i]
            sin = (beauty_cover[0][1] - beauty_cover[i][1]) / ((beauty_cover[0][1] - beauty_cover[i][1]) ** 2 + (
            beauty_cover[0][0] - beauty_cover[i][0]) ** 2) ** 0.5
            cos = (beauty_cover[0][0] - beauty_cover[i][0]) / ((beauty_cover[0][1] - beauty_cover[i][1]) ** 2 + (
            beauty_cover[0][0] - beauty_cover[i][0]) ** 2) ** 0.5
            new1_nobeauty_obl = []
            new2_nobeauty_obl = []
            for point in not_beauty_obl:
                new1_nobeauty_obl.append([point[0] - new_center[0], point[1] - new_center[1]])
                new2_nobeauty_obl.append([new1_nobeauty_obl[-1][0] * cos + new1_nobeauty_obl[-1][1] * sin,
                                          -new1_nobeauty_obl[-1][0] * sin + new1_nobeauty_obl[-1][1] * cos])

        flag = 'good'
        for element in new2_nobeauty_obl:
            if element[1] >= 0:
                flag = 'bad'
                break
        if flag == 'good':
            break

    if flag == 'good':
        print('Yes')
    else:
        print('No')


