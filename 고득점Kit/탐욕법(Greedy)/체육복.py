def solution(n, lost, reserve):
    #정렬되지 않았을 경우를 생각하자!!! 
    reserve = sorted(reserve)
    
    
    new_reserve = []
    for item in reserve:
        if item not in lost :
            new_reserve.append(item)
        # lost에서 빼주는 걸 빼먹어서 이거 찾는게 오래걸렸어
        else:
            lost.remove(item)
    for item in new_reserve:
        if item-1 in lost:
            lost.remove(item-1)
        elif item+1 in lost:
            lost.remove(item+1)
    answer = n - len(lost)
    return answer