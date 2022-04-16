import copy

def check_ans(N, ent, lock_start):
    for i in range(N):
        for j in range(N):
            if ent[lock_start+i][lock_start+j] == 0:
                return False
    return True

def xor(a,b):
    return (not a and b) or (a and not b)

def insert_key(key, ent, x, y):
    for i, row in enumerate(key):
        for j, item in enumerate(row):
            ent[x+i][y+j] = xor(ent[x+i][y+j], item)
            if ent[x+i][y+j] == True :
                ent[x+i][y+j] = 1
            elif ent[x+i][y+j] == False:
                ent[x+i][y+j] = 0           
    return ent

def rotation(key):
    new_key = []
    for i in range(len(key)) :
        row = []
        for j in range(len(key)):
            row.append(key[j][i])
        new_key.append(row[::-1])
    return new_key        
        

def solution(key, lock):
    keys = []
    for i in range(4):
        key = rotation(key)
        keys.append(key)
    M = len(key)
    N = len(lock)
    ent_side = 2*M+N-2
    lock_start = M-1
    lock_end = M+N-1
    ent = [ [0 for j in range(ent_side)] for i in range(ent_side)]
    for i, row in enumerate(lock):
        for j, item in enumerate(row):
            ent[lock_start+i][lock_start+j] = item
            
    for i, rot in enumerate(keys):
        for i in range(lock_end):
            for j in range(lock_end):
                new_ent = insert_key(rot, copy.deepcopy(ent), i, j)
                if check_ans(N, new_ent, lock_start) == True:
                    return True
    return False