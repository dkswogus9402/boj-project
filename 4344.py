num = int(input())

for i in range(num):
    A = list(map(int, input().split()))
    max_num = A[0]
    scores = A[1:max_num+1]
    len_scores = len(scores)
    sum_scores = sum(scores)

    aver = sum_scores / len_scores
  
    count = 0
    for check in scores:
        if check > aver:
            count += 1
    
    result = count/len_scores * 100

    print("{:.3f}%".format(result))
