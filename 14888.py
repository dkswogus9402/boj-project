N = 6
input_list = [1, 2, 3, 4, 5, 6]
operator = {
    '+' : 2,
    '-' : 1,
    '*' : 1,
    '//' : 1
    } # 덧셈, 뺄셈, 곱셈, 나눗셈
oper = ['+', '+', '-', '*', '//']
oper_count = [False] * (N-1)
result = [0] * 5

totals = []

def dfs(depth):
    if depth == 5:
        temp = ""
        total = input_list[0]
        for idx in range(len(input_list) -1):
            temp = (str(total) + result[idx] + str(input_list[idx+1]))
            print(temp)
            total = eval(temp)
        print(result)
        print(total)
        totals.append(total)
        return

    for i in range(5):
        if oper_count[i] == False:
            oper_count[i] = True
            result[depth] = oper[i] # 함
            dfs( depth+1 )
            oper_count[i] = False
dfs(0)

print(min(totals))
print(max(totals))