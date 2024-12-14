with open('Inputs/day_14.txt','r') as file:
    lines = file.readlines()
    
data = []
for line in lines:
    row = list(map(int,line.replace("p", "").replace('v',',').replace('=','').replace(' ','').replace('\n','').split(",")))
    data.append(row)


pos = []
for row in data:
    x=(row[0]+100*row[2])%101
    y=(row[1]+100*row[3])%103
    pos.append([x,y])


q1 = 0
q2 = 0
q3 = 0
q4 = 0



for row in pos:
    x = row[0]
    y = row[1]
    if x < 50 and y <51:
        q1 = q1+1
    elif x < 50 and y > 51:
        q2 = q2 + 1
    elif x > 50 and y > 51:
        q3 = q3 + 1
    elif x > 50 and y < 51:
        q4 = q4 + 1


print(q1 * q2 * q3 * q4)


check = ""
i=-94
while check == "":
    i += 101
    data_2 = [[" " for y in range(101) ] for x in range(103) ]
    for row in data:
        x=(row[0]+i*row[2])%101
        y=(row[1]+i*row[3])%103
        data_2[y][x] = "O"
    print("Result for i = " +str(i))
    for row in data_2:
        print(row)
    check = input()