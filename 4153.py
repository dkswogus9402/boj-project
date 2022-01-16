while True:
    A, B, C = map(int, input().split())
    
    if A == 0 and B == 0 and C == 0:
        break
    
    ABC_list = [A, B, C]
    ABC_list.sort()

    if ABC_list[2]**2 == ABC_list[1]**2 + ABC_list[0]**2:
        print("right")
    else:
        print("wrong")