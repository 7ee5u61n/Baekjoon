K, Q, R, B, Kn, P = map(int, input().split()) # 주어진 킹, 퀸, 룩, 비숍, 나이트, 폰 개수

setK = 1
setQ = 1
setR = 2
setB = 2
setKn = 2
setP = 8

print(setK - K, setQ - Q, setR - R, setB - B, setKn - Kn, setP - P)