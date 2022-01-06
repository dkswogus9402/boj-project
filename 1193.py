num = int(input())
line = 0
end = 0

while num > end:
    line += 1
    end += line

diff = end - num

if line % 2 == 0:
    A = line - diff
    B = diff + 1
else :
    B = line - diff
    A = diff + 1

print(f"{A}/{B}")