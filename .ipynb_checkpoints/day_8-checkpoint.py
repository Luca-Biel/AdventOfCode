import time
start = time.process_time()

with open('Inputs/day_8.txt','r') as file:
    lines = file.readlines()
    
data = []
for line in lines:
    row = list(line.replace('\n', ''))
    data.append(row)
	
def get_all_indices(data, l, w, lov):
    res_x = []
    res_y = []
    for x in range(0,w):
        for y in range(0,l):
            if data[y][x] == lov:
                res_x.append(x)
                res_y.append(y)
    return [res_x,res_y]
	
def get_sol_pos(pair):
    dist = pair[0] - pair[1]
    sol1 = pair[0] + dist
    sol2 = pair[1] - dist
    return [sol1,sol2]

def check_limits(val,lim):
    if val<lim and val >= 0:
        return 1
    else:
        return 0

def calc_inter(x1,x2,y1,y2,w,l):
    x=get_sol_pos([x1,x2])
    y=get_sol_pos([y1,y2])
    sol = []
    if check_limits(x[0],w) * check_limits(y[0],l) == 1:
        sol.append([x[0],y[0]])
        
    if check_limits(x[1],w) * check_limits(y[1],l) == 1:
        sol.append([x[1],y[1]])
    return sol

# get all tower names	
pos=[]
for row in data:
    for item in row:
        if item not in pos and item != '.':
            pos.append(item)

l=len(data)
w=len(data[0])


# check for deps
inter=[]
for p in pos:
    ind = get_all_indices(data,l,w,p)
    lp = len(ind[0])
    for i in range(0,lp-1):
        for j in range (i+1,lp):
            inter_res = calc_inter(ind[0][i],ind[0][j],ind[1][i],ind[1][j],w,l)
            for row in inter_res:
                inter.append(row)
				
res=[]
for row in inter:
    if row not in res:
        res.append(row)
		
print("Number of Inters with dist: " + str(len(res)))

def get_line(x1,x2,y1,y2,w,l):
    sol = [[x1,y1]]
    xdist = x1-x2 
    ydist = y1-y2 
    mdist = max(abs(ydist),abs(xdist))
    hit = False
    uplim = False
    downlim = False
    while hit == False:
        if xdist % (mdist) == 0 and ydist % (mdist) == 0:
            hit = True
            x = xdist / mdist
            y = ydist / mdist
        mdist = mdist-1
    xsol = x1
    ysol = y1
    while uplim == False:
        xsol = xsol + x
        ysol = ysol + y
        if xsol < w and ysol < l and xsol >= 0 and ysol >= 0:
            sol.append([xsol,ysol])
        else:
            uplim = True
    xsol = x1
    ysol = y1
    while downlim == False:
        xsol = xsol - x
        ysol = ysol - y
        if xsol < w and ysol < l and xsol >= 0 and ysol >= 0:
            sol.append([xsol,ysol])
        else:
            downlim = True
    return sol
	
inter=[]
for p in pos:
    ind = get_all_indices(data,l,w,p)
    lp = len(ind[0])
    for i in range(0,lp-1):
        for j in range (i+1,lp):
            inter_res = get_line(ind[0][i],ind[0][j],ind[1][i],ind[1][j],w,l)
            for row in inter_res:
                inter.append(row)
				
				
res=[]
for row in inter:
    if row not in res:
        res.append(row)

print("Number of Inters in line: " + str(len(res)))


# your code here    
print(str(time.process_time() - start) + " Sec")