input_list = input()
sort_list = []
for value in input_list:
    sort_list.append(value)
sort_list.sort(reverse = True)

print(''.join(sort_list))