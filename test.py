T = int(input())
for test_case in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    correct = True
    # 행
    for i in range(9):
        # print(sudoku[i], i)
        s = set()
        for j in range(9):
            s.add(sudoku[i][j])
        
        if len(s) != 9:
            correct = False
            break
    # print(correct, '행')
    
    # 열
    if correct:
        for i in range(9):
            s = set()
            for j in range(9):
                s.add(sudoku[j][i])
            
            if len(s) != 9:
                correct = False
                break
    # print(correct, '열')

    # 3*3
    if correct:
        for bi in range(3):
            for bj in range(3):
                s = set()
                for ai in range(3):
                    for aj in range(3):
                        s.add(sudoku[bi*3+ai][bj*3+aj])
                
                if len(s) != 9:
                    correct = False
                    break
    # print(correct, '3*3')
    
    if correct:
        print(f'Case {test_case}: CORRECT')
    else:
        print(f'Case {test_case}: INCORRECT')
    
    if test_case < T:
        input()