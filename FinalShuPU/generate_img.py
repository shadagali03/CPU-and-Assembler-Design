# Sarang Hadagali and Dev Patel
# I pledge my honor that I have abided by the Stevens Honor System

# gets the path name from user
path_name = input()

instruction_hash = {
    'sum':  '01',
    'diff':  '00',
    'load' : '10',
    'store': '11',
    'r0':   '00',
    'r1':   '01',
    'r2':   '10',
    'r3':   '11'
}

# Assume that file is in the same directory of program
inst_list = []
with open(path_name, 'r') as instructions:
    while True:
        line = instructions.readline()
        if not line:
            break
        inst_list.append(line.split())

# Create file
binary_code = open('machine_code.txt','w')

def defualt_text():
    op_list = []
    op_list.append(['v3.0 hex words addressed'])
    op_list.append(['00:'])
    op_list.append(['10:'])
    op_list.append(['20:'])
    op_list.append(['30:'])
    op_list.append(['40:'])
    op_list.append(['50:'])
    op_list.append(['60:'])
    op_list.append(['70:'])
    op_list.append(['80:'])
    op_list.append(['90:'])
    op_list.append(['a0:'])
    op_list.append(['b0:'])
    op_list.append(['c0:'])
    op_list.append(['d0:'])
    op_list.append(['e0:'])
    op_list.append(['f0:'])
    return op_list
def data_text():
    data_list = []
    data_list.append(['v3.0 hex words addressed'])
    data_list.append(['00:'])
    return data_list
    

op_list = defualt_text()
count = 0
for instruction in inst_list:
    if instruction[0] == 'data':
        break
    bin = ''
    if instruction[0] == 'load' or instruction[0] == 'store':
        if instruction[0] == 'load':
            bin += instruction_hash['load']
        else:
            bin += instruction_hash['store']
        bin += instruction_hash[instruction[1]]
        num = format(int(instruction[2]), 'b')
        for i in range(4-len(num)):
            num = '0' + num
        bin += num
        op_list[(count//16)+1].append(hex(int(bin,2))[2:])
    else:
        for word in instruction:
            bin += instruction_hash[word]
        op_list[(count//16)+1].append(hex(int(bin,2))[2:])
    count += 1

for list in op_list:
    if list[0] == 'v3.0 hex words addressed':
        continue
    for i in range(17-len(list)):
        list.append('00')
        
for list in op_list:
    for code in list:
        binary_code.write(code + ' ')
    binary_code.write('\n')
binary_code.close()

data_list = data_text()

def twos_comp(bin):
    newBin = ''
    for bit in bin:
        if bit == '0':
            newBin += '1'
        else:
            newBin += '0'
    newBin = int(newBin,2) + 1
    return newBin
    

data_count = 0
for i in range(count+1, len(inst_list)-1):
    if inst_list[i][-1][0] == '-':
        two_comp = format(int(inst_list[i][-1][1:]), 'b')
        for j in range(8-len(two_comp)):
            two_comp = '0' + two_comp
        test = twos_comp(two_comp)
        data_list[(data_count//16)+1].append(hex(int(test))[2:])
    else:
        data_list[(data_count//16)+1].append(hex(int(inst_list[i][-1]))[2:])
    data_count += 1

data_code = open('data_code.txt', 'w')

for list in data_list:
    if list[0] == 'v3.0 hex words addressed':
        continue
    for i in range(17-len(list)):
        list.append('00')

for list in data_list:
    for code in list:
        data_code.write(code + ' ')
    data_code.write('\n')
data_code.close()

instructions.close()
