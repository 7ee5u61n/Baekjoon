promise = {'Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 
           'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop'}

n = int(input())
result = False
for _ in range(n):
    line = input()
    if line not in promise:
        result = True

if result:
    print("Yes")
else:
    print("No")