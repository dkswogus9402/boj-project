def fibo(num):
    global memory, zero_cnt, one_cnt
    # 메모이제이션을 활용한 풀이
    # 만약 memory의 길이보다 작다면 해당 값을 불러오기만 함
    if len(memory) > num:
        z_c, o_z = memory_cnt[num]
        zero_cnt += z_c
        one_cnt += o_z
        return memory[num]
    
    # 메모리에 없다면, 해당 값을 메모리에 추가시켜줌
    memory.append(fibo(num-1) + fibo(num-2))
    memory_cnt.append([zero_cnt, one_cnt])
    # 추가시킨 메모리의 마지막 값 호출
    return memory[-1]



T = int(input())
for tc in range(1, 1+T):

    one_cnt = 0
    zero_cnt = 0
    memory_cnt = [[1, 0],[0, 1]]
    memory = [1,1]

    input_num = int(input())
    fibo(input_num)
    print(*memory_cnt[input_num])   
