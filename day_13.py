with open('Inputs/day_13.txt','r') as file:
    lines = file.readlines()
    
data = []
for line in lines:
    row = list(line.replace(":", ",").replace('X','').replace('+','').replace('=','').replace('Y','').replace('\n','').replace(' ','').split(","))
    data.append(row)

def solve_equation(ax,ay,bx,by,tx,ty):
    v = 1.0 * ((tx * ay) - (ty * ax))/((ay * bx) - (by * ax))
    u1 = (tx - bx * v) / ax
    u2 = (ty - by * v) / ay
    if u1 == u2 and u1 % 1 == 0 and v % 1 == 0 and u1 >= 0 and v >= 0:
        return([u1,v])
    else:
        return [0,0]
	
work=[]
for i in range(0,int(len(data)/4)+1):
    ax = int(data[i*4][1])
    ay = int(data[i*4][2])
    bx = int(data[i*4+1][1])
    by = int(data[i*4+1][2])
    tx = int(data[i*4+2][1])
    ty = int(data[i*4+2][2])
    work.append([ax,ay,bx,by,tx,ty])
	
tokens=0
for row in work:
    sol = solve_equation(row[0],row[1],row[2],row[3],row[4],row[5])
    tokens = tokens + 3 * sol[0] + sol[1]
print(tokens)


work=[]
for i in range(0,int(len(data)/4)+1):
    ax = int(data[i*4][1])
    ay = int(data[i*4][2])
    bx = int(data[i*4+1][1])
    by = int(data[i*4+1][2])
    tx = int(data[i*4+2][1])
    ty = int(data[i*4+2][2])
    work.append([ax,ay,bx,by,tx+10000000000000,ty+10000000000000])
	
tokens=0
for row in work:
    sol = solve_equation(row[0],row[1],row[2],row[3],row[4],row[5])
    tokens = tokens + 3 * sol[0] + sol[1]
print(tokens)