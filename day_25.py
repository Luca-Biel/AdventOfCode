with open('Inputs/day_25.txt','r') as file:
    lines = file.readlines()

data = []
keys = []
locks = []
for line in lines:
    row = list(line.replace('\n',''))
    if len(row) > 1:
        data.append(row)
    
def test_col(tr,p):
    counter = 0
    for j in range(7):
        if data[tr+j][p] == '#':
            counter = counter+1
    return(counter)

def test_set(tr):
    set_val = []
    for c in range(5):
        set_val.append(test_col(tr,c))
    return(set_val)

def test_type(tr):
    if data[tr] == ['#','#','#','#','#']:
        return('lock')
    elif data[tr + 6] == ['#','#','#','#','#']:
        return('key')
    else:
        print('Error')
		
for i in range(0,int(len(data)/7)):
    toprow = i * 7
    sol = test_set(toprow)
    kl_type = test_type(toprow)
    if kl_type == 'key':
        keys.append(sol)
    if kl_type == 'lock':
        locks.append(sol)
		
counter = 0
for key in keys:
    for lock in locks:
        if key[0] + lock[0] <= 7 and key[1] + lock[1] <= 7 and key[2] + lock[2] <= 7 and key[3] + lock[3] <= 7 and key[4] + lock[4] <= 7:
            counter = counter + 1
			
print(counter)