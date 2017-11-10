with open('input.txt') as f:
    diary_string = f.readline().strip().split('.')

    if diary_string.count('') > 1:
        print(-1)
    else:
        new_list = []
        for element in diary_string:
            new_element = element.strip().capitalize().split()
            new_sentence = ' '.join(new_element)
            new_list.append(new_sentence)
            new_str = '. '.join(new_list).strip()
        print(new_str)

