# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

num = int(input())

nums = list(map(int, input().split()))

result = 0

for value in nums:
    count = 0
    for i in range(1, value+1):
        if value % i == 0:
            count +=1
    if count == 2:
        result +=1
    
print(result)