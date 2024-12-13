with open('Inputs/day_12.txt','r') as file:
    lines = file.readlines()
    
data = []
for line in lines:
    row = list(line.replace('\n',''))
    data.append(row)
	
maxx = len(data[0])
maxy = len(data)
overall=[]
results=[]
for k in range(0,maxy):
    for l in range(0,maxx):
        if [k,l] not in overall:
            field = data[k][l]
            group = [[k,l]]
            i = 0
            border = 0
            while i < len(group):
                y = group[i][0]
                x = group[i][1]
                if y == 0:
                    border = border + 1
                else:
                    if data[y-1][x] == field:
                        if [y-1,x] not in group:
                            group.append([y-1,x])
                    else:
                        border = border + 1

                if x == 0:
                    border = border + 1
                else:
                    if data[y][x-1] == field:
                        if [y,x-1] not in group:
                            group.append([y,x-1])
                    else:
                        border = border + 1
                if y >= maxy - 1:
                    border = border + 1
                else:
                    if data[y+1][x] == field:
                        if [y+1,x] not in group:
                            group.append([y+1,x])
                    else:
                        border = border + 1
                if x >= maxx - 1:
                    border = border + 1
                else:
                    if data[y][x+1] == field:
                        if [y,x+1] not in group:
                            group.append([y,x+1])
                    else:
                        border = border + 1
                i = i + 1
            for row in group:
                overall.append(row)
            results.append([len(group),border])
			
			
score = 0
for row in results:
    score = score + row[0] * row[1]
print(score)

maxx = len(data[0])
maxy = len(data)
overall=[]
results=[]
for k in range(0,maxy):
    for l in range(0,maxx):
        if [k,l] not in overall:
            field = data[k][l]
            group = [[k,l]]
            i = 0
            border = 0
            while i < len(group):
                y = group[i][0]
                x = group[i][1]
                
                # check up
                if y == 0:
                    if x == 0:
                        border = border + 1
                    elif data[y][x-1] != field:
                        border = border + 1                        
                else:
                    if data[y-1][x] == field:
                        if [y-1,x] not in group:
                            group.append([y-1,x])
                    else:
                        if x == 0:
                            border = border + 1
                        elif data[y][x-1] != field:
                            border = border + 1 
                        elif data[y-1][x-1] == field:
                            border = border + 1 
                # check left
                if x == 0:
                    if y == 0:
                        border = border + 1
                    elif data[y-1][x] != field:
                        border = border + 1    
                else:
                    if data[y][x-1] == field:
                        if [y,x-1] not in group:
                            group.append([y,x-1])
                    else:
                        if y == 0:
                            border = border + 1
                        elif data[y-1][x] != field:
                            border = border + 1 
                        elif data[y-1][x-1] == field:
                            border = border + 1 
                # check below
                if y >= maxy - 1:
                    if x == 0:
                        border = border + 1
                    elif data[y][x-1] != field:
                        border = border + 1     
                else:
                    if data[y+1][x] == field:
                        if [y+1,x] not in group:
                            group.append([y+1,x])
                    else:
                        if x == 0:
                            border = border + 1
                        elif data[y][x-1] != field:
                            border = border + 1
                        elif data[y+1][x-1] == field:
                            border = border + 1  
                # check right
                if x >= maxx - 1:
                    if y == 0:
                        border = border + 1
                    elif data[y-1][x] != field:
                        border = border + 1  
                else:
                    if data[y][x+1] == field:
                        if [y,x+1] not in group:
                            group.append([y,x+1])
                    else:
                        if y == 0:
                            border = border + 1
                        elif data[y-1][x] != field:
                            border = border + 1 
                        elif data[y-1][x+1] == field:
                            border = border + 1  
                i = i + 1
            for row in group:
                overall.append(row)
            results.append([len(group),border])
			
score = 0
for row in results:
    score = score + row[0] * row[1]
print(score)