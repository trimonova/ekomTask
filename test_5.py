with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    print(n, m)
    resource_dict = {}
    resource_list_check = []
    for i in range(n):
        resource_dict[i] = set()

    for line in f:
        s, l, r, d = map(int, line.split())
        time_set = set(range(s, d+1))
        for resource in range(l, r+1):
            reserved_time = resource_dict[resource]
            if len(reserved_time.union(time_set)) == len(time_set) + len(reserved_time):
                resource_list_check.append(1)
        if len(resource_list_check) == r - l + 1:
            for resource in range(l, r + 1):
                resource_dict[resource].union(time_set)



