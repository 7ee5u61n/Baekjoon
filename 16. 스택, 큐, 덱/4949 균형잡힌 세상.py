import sys
        
while True:
    T = sys.stdin.readline().rstrip()
    if T == '.':
        break
    
    stack = []
    
    for i in T:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop() # 마지막이 소괄호면 삭제
            else:
                stack.append(i)
                break

        elif i == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop() # 마지막이 대괄호면 삭제
            else:
                stack.append(i)
                break
            
    if stack: # 리스트에 값이 있을 때
        print('no') 
    else:
        print('yes')