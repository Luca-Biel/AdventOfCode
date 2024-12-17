junctions = [[1,0,0,1,139,'E',1,0]]
junctions_check = []
minima = {0: 0}
with open('Inputs/day_16.txt','r') as file:
    lines = file.readlines()
    
data_map = []
for line in lines:
    row = list(line.replace('\n',''))
    data_map.append(row)


def check_path(dire,x,y):
    if dire == 'E':
        x=x+1
    elif dire == 'N':
        y=y-1
    elif dire == 'W':
        x=x-1
    elif dire == 'S':
        y=y+1
    if data_map[y][x] == '.':
        return(1)
    elif data_map[y][x] == 'E':
        return(99)
    else:
        return(0)

def check_possibilities(dire,x,y):
    if dire == 'E':
        x=x+1
    elif dire == 'N':
        y=y-1
    elif dire == 'W':
        x=x-1
    elif dire == 'S':
        y=y+1
    #straight
    left = int((dirdict2[dire] + 1) % 4)
    right = int((dirdict2[dire]  - 1) % 4)
    a = check_path(dire,x,y)
    b = check_path(dirdict[left],x,y)
    c = check_path(dirdict[right],x,y)
    return([a,b,c,x,y,dire])
    



dirdict={0:'E',1:'N',2:'W',3:'S'}
dirdict2={'E':0,'N':1,'W':2,'S':3}


for i in range(500000):
    x_pos = junctions[i][3]
    y_pos = junctions[i][4]
    sdir = junctions[i][5]
    points = junctions[i][6]
    progr = True
    while progr == True:
        junctions_temp = []
        cp = check_possibilities(sdir,x_pos,y_pos)
        x_pos = cp[3]
        y_pos = cp[4]
        if sum(cp[0:3]) == 1:
            if cp[1] == 1:
                sdir = dirdict[int((dirdict2[sdir] + 1) % 4)]
                points = points + 1001
            elif cp[2] == 1:
                sdir = dirdict[int((dirdict2[sdir] - 1) % 4)]
                points = points + 1001
            else:
                points = points + 1
        elif sum(cp[0:3]) == 0:
            progr = False
            junctions[i][7] = 0
        elif sum(cp[0:3]) > 10:
            print("found_exit")
            print(points+1)
        elif sum(cp[0:3]) > 1:
            progr = False
            if cp[0] == 1:
                j_points = points + 1
                junctions_temp.append([cp[0],cp[1],cp[2],cp[3],cp[4],sdir,j_points,1])
            if cp[1] == 1:
                j_dir = dirdict[int((dirdict2[sdir] + 1) % 4)]
                j_points = points + 1001
                junctions_temp.append([cp[0],cp[1],cp[2],cp[3],cp[4],j_dir,j_points,1])
            if cp[2] == 1:
                j_dir = dirdict[int((dirdict2[sdir] - 1) % 4)]
                j_points = points + 1001
                junctions_temp.append([cp[0],cp[1],cp[2],cp[3],cp[4],j_dir,j_points,1])
        for row in junctions_temp:
            check = [row[3],row[4],row[5]]
            check_str = str(row[3]) + ' ' + str(row[4]) + ' ' + str(row[5])
            if check not in junctions_check:
                junctions.append(row)
                junctions_check.append(check)
                minima.update({check_str: row[6]}) 
            elif row[6] < minima[check_str]:
                minima.update({check_str: row[6]}) 
                junctions.append(row)