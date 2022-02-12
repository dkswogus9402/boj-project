input_list = []

for i in range(9):
    input_li = list(map(int, input().split()))
    input_list.append(input_li)

# 백트래킹을 사용해야 하기 때문에 빈칸을 찾는 것이 우선
zeros = [[i,j] for i in range(9) for j in range(9) if input_list[i][j] == 0]

# 조건 : 1. 같은 행과 2. 같은 열에 같은 숫자가 들어가면 안됨, 3.사각형 안에 같은 숫자가 들어가면 안됨
# 같은 행에 숫자가 있는지 확인

def promising(i,j): # 좌표를 받아옴
    count = [False for _ in range(10)] # 헤일리 코드 보고 배움
    for k in range(9): # 조건 1, 2에 해당되는 부분
        count[input_list[i][k]] = True
        count[input_list[k][j]] = True

    #3 * 3 행렬의 시작 위치를 구하고 돌림  # 조건 3에 해당하는 부분
    temp_i = i//3 * 3; temp_j = j//3 * 3 
    for q in range(temp_i, temp_i+3):
        for w in range(temp_j, temp_j+3):
            count[input_list[q][w]] = True

    # 후보 군들을 구함 count를 처음에 10개 선언하고 0은 제외하고 선별함
    victims = []
    for idx, value in enumerate(count[1:]):
        if value == False:
            victims.append(idx + 1)
    return victims

def dfs(depth):
    global flag
    if flag == 1:
        return

    if depth == len(zeros):
        flag = 1
        for i in range(len(input_list)):
            print(*input_list[i])
        return

    i,j = zeros[depth]
    victims = promising(i,j)
    # 이 부분이 제일 힘들었음.
    # 스도쿠를 안하다 보니.. 해당되는 정답자리에는 정답후보군이 아니라 정답이 들어와야 한다고.. 생각함..
    # 이후에 정답을 넣어주는 것 대신 정답 후보군을 넣어줘서 해결함 (다른 사람이 푼 방식을 참고해서 알아냈습니다..)
    for victim in victims:
        input_list[i][j] = victim
        dfs(depth+1)
        input_list[i][j] = 0

flag = 0
dfs(0)