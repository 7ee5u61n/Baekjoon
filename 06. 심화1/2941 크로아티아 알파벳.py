# 크로아티아 알파벳
# ć 	c-
# dž 	dz=
# đ 	d-
# lj 	lj
# nj 	nj
# š 	s=
# ž     z=
croatian = ['c=','c-','dz=','d-','lj','nj','s=','z=']
N = str(input()) # 알파벳 입력

for i in croatian:
    if i in N:
        N = N.replace(i,' ') # 크로아티아 알파벳이 나오면 단어에서 삭제

print(len(N))