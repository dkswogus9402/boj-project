import sys
input = sys.stdin.readline

M, N = map(int, input().split())

dogam =  {i+1:input().rstrip() for i in range(M)}
dogam_num =  {value : key for key, value in dogam.items()}

for i in range(N):
    A = input().rstrip()
    if A.isalpha():
        print(dogam_num[A])
    else:
        A = int(A)
        print(dogam[A])
