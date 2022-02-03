import sys
input = sys.stdin.readline

# num = int(input())
# input_list = []
# for _ in range(num):
#     input_num = int(input())
#     input_list.append(input_num)

# result = [0] * num

# counting = {}

# for key in set(input_list): # 시간이 좀 걸릴 듯
#     counting[key] = 0

# for key in input_list: # 카운팅 합
#     counting[key] += 1

# total = 0
# total_counting = {}
# for key, value in counting.items(): # 누적 합
#     total += value
#     total_counting[key] = total

# for number in input_list[::-1]: # 카운팅 합
#     value = total_counting.get(number)
#     result[value - 1] = number
#     total_counting[number] -= 1

# for value in result:
#     print(value)

# 카운팅 정렬 #

# counting sort에서 빈도 저장하기 위한 배열
import sys
input = sys.stdin.readline
li = [0 for _ in range(10001)]

N = int(input())

# 굳이 딕셔너리에 저장할 필요가 없음 숫자이니까.
for _ in range(N):
    num = int(input())
    li[num] += 1 # 각 숫자에 해당하는 인덱스에 플러스를 하면 좋음

# 배열의 시작부터 돌며 저장된 빈도만큼 인덱스값을 출력
for i in range(1, 10001):
    count = li[i]
    for _ in range(count):
        print(i)