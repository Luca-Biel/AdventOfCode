with open('Inputs/day_15.txt','r') as file:
    lines = file.readlines()
    
data_map = []
data_move = []
for line in lines:
    row = list(line.replace('\n',''))
    if len(row) == 0:
        print(row)
    elif row[0] == '#':
        data_map.append(row)
    elif row[0] in ['v','<','>','^']:
        for item in row:
            data_move.append(item)
        
for x in range (len(data_map[0])):
    for y in range (len(data_map)):
        if data_map[y][x] == '@':
            x_pos = x
            y_pos = y



def move_stuff(x,y,direction,set_val):    
    changes = []
    if direction == '^':
        y=y-1
    elif direction == '>':
        x=x+1
    elif direction == 'v':
        y=y+1
    elif direction == '<':
        x=x-1
    if data_map[y][x] == '#':
        changes.append([0,0,''])
    elif data_map[y][x] == 'O':
        enum = move_stuff(x,y,direction,'O')
        for row in enum:
            changes.append(row)
        changes.append([x,y,set_val])
    elif data_map[y][x] == '.':
        changes.append([x,y,set_val])
    else:
        print('Error')
        print(data_map[y][x])
        print(x)
        print(y)
    return changes


for mi in data_move:
    adjust = move_stuff(x_pos,y_pos,mi,'@')
    if [0,0,''] not in adjust:
        for row in adjust:
            data_map[row[1]][row[0]] = row[2]
        data_map[y_pos][x_pos] = '.'
        y_pos = row[1]
        x_pos = row[0]


total = 0
for x in range(len(data_map[0])):
    for y in range(len(data_map)):
        if data_map[y][x] == 'O':
            total = total + 100 * y + x
total



# Part 2 - not removed debugging part (IPYNB doesn't work)

with open('Inputs/day_15.txt','r') as file:
    lines = file.readlines()
    
data_map_2 = []
data_move = []
for line in lines:
    row = list(line.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.').replace('\n',''))
    if len(row) == 0:
        print(row)
    elif row[0] == '#':
        data_map_2.append(row)
    elif row[0] in ['v','<','>','^']:
        for item in row:
            data_move.append(item)
		
def move_stuff_2(x,y,direction,set_val,dontgo):  
    changes = [[x,y,'.']]
    if set_val == ']':
        changes.append([x-1,y,'.'])
    elif set_val == '[':
        changes.append([x+1,y,'.'])
    if direction == '^':
        y=y-1
        ver = True
    elif direction == '>':
        x=x+1
        ver = False
    elif direction == 'v':
        y=y+1
        ver = True
    elif direction == '<':
        x=x-1
        ver = False
    if data_map_2[y][x] == '#':
        changes.append([0,0,''])
    elif data_map_2[y][x] == '[':
        if ver == False:
            enum = move_stuff_2(x,y,direction,'[','')
            for row in enum:
                changes.append(row)
        elif dontgo != 'l':
            enum = move_stuff_2(x,y,direction,'[','')
            for row in enum:
                changes.append(row)
            enum = move_stuff_2(x+1,y,direction,']','r')
            for row in enum:
                changes.append(row)
        changes.append([x,y,set_val])
    elif data_map_2[y][x] == ']':
        if ver == False:
            enum = move_stuff_2(x,y,direction,']','')
            for row in enum:
                changes.append(row)
        elif dontgo != 'r':
            enum = move_stuff_2(x,y,direction,']','')
            for row in enum:
                changes.append(row)
            enum = move_stuff_2(x-1,y,direction,'[','l')
            for row in enum:
                    changes.append(row)
        changes.append([x,y,set_val])
    elif data_map_2[y][x] == '.':
        changes.append([x,y,set_val])
    elif data_map_2[y][x] == ']' and dontgo == 'r':
        True
    elif data_map_2[y][x] == '[' and dontgo == 'l':
        True
    else:
        print('Error')
        print(data_map_2[y][x])
        print(x)
        print(y)
    return changes


for x in range (len(data_map_2[0])):
    for y in range (len(data_map_2)):
        if data_map_2[y][x] == '@':
            x_pos = x
            y_pos = y

y_b = 0
x_b = 0
i = 0
for mi in data_move:
    i = i+1
    adjust = move_stuff_2(x_pos,y_pos,mi,'@','')
    if [0,0,''] not in adjust:
        for row in adjust:
            if row[2] == '.':
                data_map_2[row[1]][row[0]] = row[2]
        for row in adjust:
            if row[2] != '.':
                data_map_2[row[1]][row[0]] = row[2]
        y_pos = row[1]
        x_pos = row[0]
    breaker=0
    for x in range(len(data_map_2[0])):
        for y in range(len(data_map_2)):
            if data_map_2[y][x] == '[' and data_map_2[y][x+1] != ']':
                breaker = 1
                x_b = x
                y_b = y
    if breaker == 1:
        for row in data_map_2:
            print(row)
        print(mi)
        print(x_pos)
        print(y_pos)
        print(x_b)
        print(y_b)
        print(i)
        
total = 0
for x in range(len(data_map_2[0])):
    for y in range(len(data_map_2)):
        if data_map_2[y][x] == '[':
            total = total + 100 * y + x
print(total)