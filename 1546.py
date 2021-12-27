N = int(input())
A = list(map(int, input().split()))

max_num = max(A)

new_scores = []

for score in A:
    new_score = score/max_num * 100
    new_scores.append(new_score)

len_scores = len(new_scores)
sum_scores = sum(new_scores)

result = sum_scores / len_scores

print("{:.5f}".format(result))