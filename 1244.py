'''
스위치는 N개이다.
1은 켜져있고, 0은 꺼져있음을 상징한다.
받은 수 : 1이상 스위치 개수 이하인 자연수를 받는다.
조건은 받은 수와 자신의 성별에 따라서 달라진다.
'''

'''

남학생은 스위치 번호가 자기가 받은 수의 배수이면 그 스위치 상태를 바꾼다.
즉 스위치가 켜져 있으면 끄고, 꺼져 있으면 스위치를 킨다.

여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서
그 구간의 스위치 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

스위치도 있고 번호도 있고 상태도 있다.

예를들어
'''
'''
1이면 0으로 만들어주고 0이면 1로 만들어준다.
'''
def change_state(i):
    if i == 1:
        return 0
    else:
        return 1

def man_acting(num, N, space):
    for i in range(N):
        if (i+1) % num == 0:
            space[i] = change_state(space[i]) 
            # 스위치의 상태를 바꾼다.

def women_acting(num, N, space):
    num = num - 1 # 0번 부터 시작하기 때문
    space[num] = change_state(space[num])
    for i in range(1, N//2+1):
        if 0 <= num - i < N and 0 <= num + i < N: # 조건 내에서
            if space[num-i] == space[num+i]: # 같다면
                space[num-i] = change_state(space[num-i])
                space[num+i] = change_state(space[num+i])
            else:   return
        else:   return

N = int(input())
iter_num = N // 20 if N % 20 == 0 else (N // 20 + 1)


A = list(map(int, input().split()))

student_num = int(input())
for i in range(student_num):
    gender, num = map(int, input().split())

    if gender == 1:
        man_acting(num, N, A)

    elif gender == 2:
        women_acting(num, N, A)

iter_num = N // 20 if N % 20 == 0 else (N // 20 + 1)

for i in range(iter_num):
    print(*A[i * 20 : (i+1) * 20])
