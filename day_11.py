data =[0, 7, 198844, 5687836, 58, 2478, 25475, 894]

def rules(n):
    nstr = str(n)
    lstr = int(len(str(nstr)))
    if n == 0:
        return [1]
    elif len(nstr) % 2 == 0:
        return [int(nstr[0:int(lstr / 2)]),int(nstr[int(lstr / 2):lstr])]
    else:
        return [n * 2024]

looper = data
for i in range(0,25):
    loop_res = []
    for item in looper:
        res=rules(item)
        for subres in res:
            loop_res.append(subres)
    looper = loop_res

print(len(looper))
# part 2


def get_iteration(data,dict_iter):
    keys=[]
    values=[]
    for row in data:
        total = 0
        for item in row[1]:
            total = total + dict_iter[item]
        keys.append(row[0])
        values.append(total)
    return dict(zip(keys, values))
		
		

pos = data
for i in range(0,5):
    dict_loop = []
    for item_base in pos:
        looper = [item_base]
        for j in range(0,15):
            loop_res = []
            for item in looper:
                res=rules(item)
                for subres in res:
                    loop_res.append(subres)
            looper = loop_res
        dict_loop.append([item_base,looper,len(looper)])
    if (i == 3):
        dict_loop_3 = dict_loop[:]
    elif (i == 2):
        dict_loop_2 = dict_loop[:]
    elif (i == 1):
        dict_loop_1 = dict_loop[:]
    elif (i == 0):
        dict_loop_0 = dict_loop[:]
    pos=[]
    for row in dict_loop:
        for item in row[1]:
            if item not in pos:
                pos.append(item)


keys=[]
values=[]
for row in dict_loop:
    keys.append(row[0])
    values.append(row[2])

my_dict_4 = dict(zip(keys, values))

my_dict_3 = get_iteration(dict_loop_3,my_dict_4)
my_dict_2 = get_iteration(dict_loop_2,my_dict_3)
my_dict_1 = get_iteration(dict_loop_1,my_dict_2)
my_dict_0 = get_iteration(dict_loop_0,my_dict_1)

keys=[]
values=[]
total = 0
for item in data:
    total = total + my_dict_0[item]

print(total)