#자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
#예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

A = int(input()); B = int(input())

prime_nums = []

for num in range(A, B+1):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        prime_nums.append(num)
    
if len(prime_nums) == 0:
    print(-1)
    
else:
    print(sum(prime_nums))
    print(min(prime_nums))
