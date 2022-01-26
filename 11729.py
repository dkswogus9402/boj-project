def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return
    hanoi(n-1, a, c, b) # a -> b로 n-1개의 원판이 이동
    print(a, c) # a -> c로 n의 원판이 이동
    hanoi(n-1, b, a, c) # b -> c로 n-1개의 원판이 이동

n = int(input())

print( 2**n - 1 )
hanoi(n, 1, 2, 3)