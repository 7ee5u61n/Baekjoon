n = int(input())
yonsei = 0
korea = 0

for i in range(n):
    university = input()
    if university == "yonsei":
        yonsei = i
    elif university == "korea":
        korea = i

if yonsei < korea:
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")