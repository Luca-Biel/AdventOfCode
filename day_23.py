with open('Inputs/day_23.txt','r') as file:
    lines = file.readlines()
    
data = []
for line in lines:
    row = list(line.replace('\n','').split('-'))
    data.append(row)
	
	
loops = []
for i in range(len(data)):
    if 't' in [data[i][0][0],data[i][1][0]]:
        for j in range(len(data)):
            if data[i][1] in data[j]:
                for k in range(len(data)):
                    if data[i][0] in data[k] and ((data[k][0] not in data[i] and data[k][0] in data[j]) or (data[k][1] not in data[i] and data[k][1] in data[j])):
                        upload = data[i][:]
                        for item in data[k]:
                            if item not in upload:
                                upload.append(item)
                        upload.sort()
                        if upload not in loops:
                            loops.append(upload)
                            
print(len(loops))
							
checked = []
connects = {}
for i in range(len(data)):
    for j in range(2):
        a=data[i][j]
        b=data[i][(j+1)%2]
        if a not in checked:
            connects.update({a:[b]})
            checked.append(a)
        else:
            prepare = connects[a]
            if b not in prepare:
                prepare.append(b)
            connects.update({a: prepare})
			
			
complete_graphs = []
maxrow = []

for item in checked:
    complete_graphs.append([item])
for row in complete_graphs:
    complete  = row[:]
    for item1 in connects[row[0]]:
        if item1 not in complete:
            NOT = 0
            for item2 in complete:
                if item1 not in connects[item2]:
                    NOT = 1
            if NOT == 0:
                complete.append(item1)
                complete.sort()
                if complete not in complete_graphs:
                    complete_graphs.append(complete)		
    if len(row) > len(maxrow):
        maxrow = row
		
print(maxrow)