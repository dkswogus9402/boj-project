num = int(input())

input_list = []

for i in range(num):
    age, name = input().split()
    age = int(age)
    input_list.append([age, name, i])

new_list = sorted(input_list, key = lambda x:(x[0],x[2]))

for age, name, order in new_list:
    print(age, name)
