import sys
N, M = map(int, input().split()) # N: 도감에 수록된 포켓몬 수, M: 맞춰야 하는 문제 개수

pokemon_name = {}
pokedex_number = {}
for i in range(N):
    i += 1
    pokemon = sys.stdin.readline().rstrip()
    pokemon_name[pokemon] = i
    pokedex_number[i] = pokemon

for i in range(M):
    find = sys.stdin.readline().rstrip()
    try:
        print(pokemon_name[find])
    except:
        print(pokedex_number[int(find)])