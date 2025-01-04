T = int(input())
for test_case in range(1, T+1):
    board = list(input() for _ in range(3))
    ox = input()
    
    arr = []
    for i in range(3):
        for j in range(3):
            arr.append(board[i][j])
    seted = False
    if not seted:
        # 가로
        for i in range(3):
            count = 0
            for j in range(3):
                if arr[3*i+j] == ox:
                    count += 1
            
            if count == 2:
                seted = True
                for j in range(3):
                    if arr[3*i+j] != ox:
                        arr[3*i+j] = ox
                        break
    if not seted:
        # 세로
        for i in range(3):
            count = 0
            for j in range(3):
                if arr[i+3*j] == ox:
                    count += 1
            if count == 2:
                seted = True
                for j in range(3):
                    if arr[i+3*j] != ox:
                        arr[i+3*j] = ox
                        break
    
    if not seted:
        # 대각선 아래
        count = 0
        for i in range(3):
            if arr[4*i] == ox:
                count += 1
        if count == 2:
            seted = True
            for i in range(3):
                if arr[4*i] != ox:
                    arr[4*i] = ox
                    break

    if not seted:
        # 대각선 위
        count = 0
        for i in range(1, 4):
            if arr[2*i] == ox:
                count += 1
        if count == 2:
            seted = True
            for i in range(1, 4):
                if arr[2*i] != ox:
                    arr[2*i] = ox
                    break
    
    # 출력
    print(f'Case {test_case}:')
    for i in range(9):
        print(arr[i], end='')
        if i%3 == 2:
            print('')