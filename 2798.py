# 공통된 상황을 구현하려는 것을 목표로 하자

# 현재 상황에서는 3개가 고정되어 있으므로, 3중 포문이 고정이다.

N, M = map(int, input().split())
input_list = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = input_list[i] + input_list[j] + input_list[k]
            if total > M:
                continue
            else:
                result = max(total, result)
print(result)