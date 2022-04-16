def turn(m, key):
    new_key = [[-1 for i in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[j][-(i+1)] = key[i][j]
    return new_key
    
def solution(key, lock):
    # 회전
    # 짝수 홀수 나누기
    m = len(key)
    new_key = key
    key_list = []
    for i in range(4):
        new_key = turn(m,new_key)
        key_list.append(new_key)
        
    print(key_list)
#     if len(key) % 2 == 1:
#         # center_index = len(key)//2
#         # key[center_index]
#         # # 가운데 고정
#         # new_key[center_index][center_index] = key[center_index][center_index]
#         # # 왼쪽 -> 위
#         # for i in range(m-center_index-1):
#         #     for j in range(m):
#         #         new_key[i][-(j+1)] = key[j][i]
#         # # 위 -> 오른
#         # for i in range(m-center_index-1):
#         #     for j in range(m):
#         #         new_key[j][-(i+1)] = key[i][j]
#         # # 오른 -> 아래
#         # for i in range(center_index+1,m):
#         #     for j in range(m):
#         #         new_key[i][j] = key[j][i]
#         # # 아래 -> 왼
            
#     else :
#         pass
    answer = True
    return answer