input_str = input()

table = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

input_str = list(input_str)

count = 0

for str_ in input_str:
    for k, table_str in enumerate(table):
        temp = list(table_str) 
        for j in temp:
            if j == str_:
                count = count + k + 3
                break
print(count)