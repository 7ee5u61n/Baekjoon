# 크로아티아 알파벳
# ć 	c-
# dž 	dz=
# đ 	d-
# lj 	lj
# nj 	nj
# š 	s=
# ž     z=

croatian = list(str(input())) # 알파벳 소문자와 -, = 입력가능
count = 0

for i in range(len(croatian)-1):
    i += 0
    if croatian[i] == 'd' and croatian[i+1] == 'z':
        count = count + 1
    elif croatian[i] == 'l' and croatian[i+1] == 'j':
        count = count + 1
    elif croatian[i] == 'n' and croatian[i+1] == 'j':
        count = count + 1
    elif croatian[i] == '-' or croatian[i] == '=':
        continue
    else:
        count = count + 1

print(count)