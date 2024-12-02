n = int(input())

arr = {'ADD':'0000', 'SUB':'0001', 'MOV':'0010', 'AND':'0011','OR':'0100',
                   'NOT':'0101','MULT':'0110', 'LSFTL':'0111', 'LSFTR':'1000',
                   'ASFTR':'1001','RL':'1010','RR':'1011'}

for _ in range(n):
    opcode, rD, rA, rB = input().split()
    machine_language = ''
    
    if opcode[-1]=='C':
        machine_language += arr.get(opcode[:-1])
        machine_language += '1'
    else:
        machine_language += arr.get(opcode)
        machine_language += '0'
    machine_language += '0'
    
    machine_language += str(bin(int(rD)))[2:].zfill(3)
    machine_language += str(bin(int(rA)))[2:].zfill(3)
    
    if machine_language[4] == '0':
        machine_language += str(bin(int(rB)))[2:].zfill(3)
        machine_language += '0'
    else:
        machine_language += str(bin(int(rB)))[2:].zfill(4)
        
    print(machine_language)