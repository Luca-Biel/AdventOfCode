
import itertools


with open('Inputs/day_7.txt','r') as file:
    lines = file.readlines()
    
data = []
for line in lines:
    row = list(map(int, line.replace(":", "").split(" ")))
    data.append(row)

# get solver for part 1

def attempt_solve(l,inp,op):
    sol = inp[1]
    for i in range(2,l):
        if op[i-2] == 0:
            sol = sol + inp[i]
        else:
            sol = sol * inp[i]
    return(sol)

tot_sol = 0
for row in data:
    l=len(row)
    target=row[0]
    op_l=list(itertools.product([0, 1], repeat=l-2))
    solved = False
    j=0
    while solved == False and j < 2**(l-2):
        att_sol = attempt_solve(l,row,op_l[j])
        if row[0] == att_sol:
            tot_sol = tot_sol + att_sol
            solved = True
        else:
            j+=1
			
			
print("part 1 solved as: " + str(tot_sol))


# get solver for part 2

def attempt_solve_concat(l,inp,op):
    sol = inp[1]
    for i in range(2,l):
        if op[i-2] == 0:
            sol = sol + inp[i]
        elif op[i-2] == 1:
            sol = sol * inp[i]
        else:
            sol = int(str(sol)+str(inp[i]))
    return(sol)


tot_sol_con = 0
for row in data:
    l=len(row)
    target=row[0]
    op_l=list(itertools.product([0, 1], repeat=l-2))
    solved = False
    j=0
    while solved == False and j < 2**(l-2):
        att_sol = attempt_solve(l,row,op_l[j])
        if row[0] == att_sol:
            tot_sol_con = tot_sol_con + att_sol
            solved = True
        else:
            j+=1
    if solved == False:
        op_l=list(itertools.product([0, 1, 2], repeat=l-2))
        j=0
        while solved == False and j < 3**(l-2):
            att_sol = attempt_solve_concat(l,row,op_l[j])
            if row[0] == att_sol:
                tot_sol_con = tot_sol_con + att_sol
                solved = True
            else:
                j+=1
				
				
print("part 2 solved as: " + str(tot_sol_con))