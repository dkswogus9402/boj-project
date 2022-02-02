import sys
from collections import Counter

input = sys.stdin.readline

num = int(input())
input_list = []
for _ in range(num):
    input_num = int(input())
    input_list.append(input_num)

input_list.sort()

cnt = Counter(input_list).most_common(2) # 가장 많이 사용된 2가지를 튜플형태로 반환 (숫자, 횟수)

len_list = len(input_list)
print(round(sum(input_list)/len_list))
print(input_list[len_list//2])
if len_list > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(input_list) - min(input_list))
