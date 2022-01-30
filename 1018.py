def check_count(input_lists):
    count_1 = 0
    for idx, input_list in enumerate(input_lists):
        # 만약에 짝수라면 
        if idx % 2 == 0:
            for i, value in enumerate(input_list):
                if i % 2 == 0:
                    if value != 'W':
                        count_1 += 1
                else:
                    if value != 'B':
                        count_1 += 1
        # 만약 홀수라면
        else:
            for i, value in enumerate(input_list):
                if i % 2 == 0:
                    if value != 'B':
                        count_1 += 1
                else:
                    if value != 'W':
                        count_1 += 1
    count_2 = 0
    for idx, input_list in enumerate(input_lists):
        # 만약에 짝수라면 
        if idx % 2 == 0:
            for i, value in enumerate(input_list):
                if i % 2 == 0:
                    if value != 'B':
                        count_2 += 1
                else:
                    if value != 'W':
                        count_2 += 1
        # 만약 홀수라면
        else:
            for i, value in enumerate(input_list):
                if i % 2 == 0:
                    if value != 'W':
                        count_2 += 1
                else:
                    if value != 'B':
                        count_2 += 1

    count = min(count_1, count_2)
    return count
M, N = map(int, input().split())

rows = M - 8 + 1
columns = N - 8 + 1
input_lists = []
for k in range(M):
    input_ = input()
    input_lists.append(input_)

counts = []
start_row = 0
end_row = 7
for row in range(rows):
    temp = input_lists[start_row : end_row + 1]
    start_column = 0
    end_column = 7
    for i in range(columns):
        input_list = []
        for value in temp:
            input_list.append(value[start_column : end_column + 1])
        counts.append(check_count(input_list))
        start_column += 1; end_column += 1
    start_row += 1; end_row += 1

print(min(counts))