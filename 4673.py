

def self_num():
    results = []
    for i in range(1, 10001):
        temp = 0
        for j in str(i):
            temp = temp + int(j) 
        result = temp + i
        results.append(result)
    return set(results)

results = self_num()
test =set(range(1, 10001))
test = test - results
test = sorted(test)
for value in test:
    print(value)