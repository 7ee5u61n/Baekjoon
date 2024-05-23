while True:
    n = int(input())
    if n == -1:
        break
    
    divisor = []
    for i in range(n): # 약수 구하기
        if n % (i+1) == 0:
            divisor.append(int(n/(i+1))) 

    divisor.remove(divisor[0]) # 자기 자신 제거
    divisor = sorted(divisor)
    sum = 0
    for i in range(len(divisor)): # 약수들의 합 구하기
        sum += divisor[i]

    result = ""
    if n == sum: # 6 = 1 + 2 + 3 형식으로 출력
        for i in divisor:
            result += str(i) + " + "
        result = result[:-2] # 끝에 + 제거
        print(n, '=',result)
    else:
        print(n, 'is NOT perfect.')
