
# M, N = map(int, input().split())
# input_ = sorted(list(input().split()))
# root = [False] * N
# result = [0] * M

# def w(depth):
#     if depth == 0:
#         return True

#     if ord(result[depth-1]) > ord(result[depth]):
#         return False
#     return True


# start = 0
# def DFS(depth):
#     if depth == M:
#         temp_len = len(set(result) & vowels)
#         if temp_len > 0 and M - temp_len > 1:
#             print(''.join(result))
#         return

#     for idx in range(start, N):
#         if root[idx] == False:
#             root[idx] = True
#             result[depth] = input_[idx]

#             if w(depth):
#                 DFS(depth+1)
#             root[idx] = False

# vowels = set(['a', 'e', 'i', 'o', 'u'])

# DFS(0)



M, N = map(int, input().split())
input_ = sorted(list(input().split()))
root = [False] * N
result = [0] * M


def DFS(depth, start):
    if depth == M:
        temp_len = len(set(result) & vowels)
        if temp_len > 0 and M - temp_len > 1:
            print(''.join(result))
        return

    for idx in range(start, N):
        if root[idx] == False:
            root[idx] = True
            result[depth] = input_[idx]
            DFS(depth+1, idx+1)
            root[idx] = False

vowels = set(['a', 'e', 'i', 'o', 'u'])

DFS(0, 0)