with open('Inputs/day_24.txt','r') as file:
    lines = file.readlines()
    
wires = {}
gates = []
for line in lines:
    if '->' in line:
        row = list(line.replace('\n','').replace('-> ','').split(' '))
        if len(row) > 1:
            gates.append(row)
    else:
        row = list(line.replace('\n','').replace(':','').split(' '))
        if len(row) > 1:
            wires.update({row[0]:int(row[1])})
    
	
killer = 1

while killer > 0:
    killer = 0
    prep_wires = wires.keys()
    for row in gates:
        a = row[0]
        b = row[2]
        r = row[1]
        t = row[3]
        if a in prep_wires and b in prep_wires and t not in prep_wires:
            if r == "AND":
                if wires[a] == 1 and wires[b] == 1:
                    wires.update({t:1})
                else:
                    wires.update({t:0})
            elif r == "OR":
                if wires[a] == 1 or wires[b] == 1:
                    wires.update({t:1})
                else:
                    wires.update({t:0})
            elif r == "XOR":
                if wires[a] + wires[b] == 1:
                    wires.update({t:1})
                else:
                    wires.update({t:0})
        elif a not in prep_wires or b not in prep_wires:
            killer = killer + 1
    print(killer)
	

zs = []
for key, value in wires.items():
    temp = [key,value]
    if temp[0][0] == 'z':
        zs.append(temp)
zs.sort()

total = 0
i = 0
for row in zs:
    total = total + row[1] * 2 ** i
    i = i + 1

print("solution step 1")	
print(total)

print("Step 2 was done manual")

gates_2 = []
for row in gates:
    gates_2.append([row[3],row[0],row[1],row[2]])
gates_2.sort()


new_base = []
for row in gates_2:
    if row[0] == 'vcv' and row[2] == 'XOR':
        appender = [row[0],'x13','AND','y13']
        exchanger = ['z13',row[1],'XOR',row[3]]
    elif row[0] == 'z13':
        appender = exchanger
    elif row[0] == 'cqm':
        appender = [row[0],'x33', 'XOR', 'y33']
        exchanger_vjv = ['vjv',row[1],'AND',row[3]]
    elif row[0] == 'vjv':
        appender = exchanger_vjv
    elif row[0] == 'mps' and row[2] == 'XOR':
        appender = [row[0],'vbw','OR','qkk']
        exchanger_z25 = ['z25',row[1],'XOR',row[3]]
    elif row[0] == 'z25':
        appender = exchanger_z25
    elif row[0] == 'vwp' and row[2] == 'XOR':
        appender = [row[0],'csn','AND','nmn']
        exchanger_z19 = ['z19',row[1],'XOR',row[3]]
    elif row[0] == 'z19':
        appender = exchanger_z19
    else:
        appender = row
    new_base.append(appender)
        


wires = {}
gates = []
for line in lines:
    if '->' in line:
        row = list(line.replace('\n','').replace('-> ','').split(' '))
        if len(row) > 1:
            gates.append(row)
    else:
        row = list(line.replace('\n','').replace(':','').split(' '))
        if len(row) > 1:
            wires.update({row[0]:int(row[1])})
wires_2 = {}
for line in lines:
    if '->' not in line:
        row = list(line.replace('\n','').replace(':','').split(' '))
        if len(row) > 1:
            wires_2.update({row[0]:[row[0]]})
killer = 1

while killer > 0:
    killer = 0
    prep_wires = wires.keys()
    for row in new_base:
        a = row[1]
        b = row[3]
        r = row[2]
        t = row[0]
        if a in prep_wires and b in prep_wires and t not in prep_wires:
            wa = wires_2[a][:]
            wb = wires_2[b][:]
            for item in wb:
                wa.append(item)
            if r == "AND":
                if wires[a] == 1 and wires[b] == 1:
                    wires.update({t:1})
                    wires_2.update({t:wa})
                else:
                    wires.update({t:0})
                    wires_2.update({t:wa})
            elif r == "OR":
                if wires[a] == 1 or wires[b] == 1:
                    wires.update({t:1})
                    wires_2.update({t:wa})
                else:
                    wires.update({t:0})
                    wires_2.update({t:wa})
            elif r == "XOR":
                if wires[a] + wires[b] == 1:
                    wires.update({t:1})
                    wires_2.update({t:wa})
                else:
                    wires.update({t:0})
                    wires_2.update({t:wa})
        elif a not in prep_wires or b not in prep_wires:
            killer = killer + 1
total = 0
for item in wires.keys():
    if item[0] in ['x','y']:
        total = total + wires[item] * 2 ** int(item[1:3])
print(total)

total = 0
for item in wires.keys():
    if item[0] in ['z']:
        total = total + wires[item] * 2 ** int(item[1:3])
print(total)


print('cqm,mps,vcv,vjv,vwp,z13,z19,z25')