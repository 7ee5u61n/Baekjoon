a1 = int(input())
a2 = int(input())
a3 = int(input())

if a1 == a2 == a3 == 60: 
    print('Equilateral') #정삼각형
elif a1 + a2 + a3 == 180 and a1 == a2 or a2 == a3 or a3 == a1:
    print('Isosceles') # 이등변삼각형
elif a1 + a2 + a3 == 180 and a1 != a2 != a3 != a1:
    print('Scalene') # 삼각형
elif a1 + a2 + a3 != 180:
    print('Error') # 아니