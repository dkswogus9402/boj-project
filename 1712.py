# 고정비용(A) : 임대료 재산세 보험료 급여
# 가변비용(B) : 재료비, 인건비

# 노트북 제조 비용 = 고정비용 + 가변비용 * (N) # N대의 노트북을 만들 시
# 노트북 가격 : C
# -> 어느 순간 총 수입이 총 비용보다 많아지게 된다 최초로 ABC가 주어졌을때 손익분기점이 언제인지

# 입력 = 3개

A, B, C = map(int,input().split())
flag = 0

if B >= C:
    print(-1)
else:
    print(int(A/(C-B)+1))
