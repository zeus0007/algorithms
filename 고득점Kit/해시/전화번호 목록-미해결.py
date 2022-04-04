def find_short_len(phone_book):
    item_len = 20
    for item in phone_book:
        if len(item) <= item_len:
            item_len = len(item)
    return item_len

def make_dict(phone_book,item_len):
    phone_dict = {}
    for item in phone_book:
        if item[:item_len] in phone_dict :
            phone_dict[item[:item_len]].append(item[item_len:])
        else:
            phone_dict[item[:item_len]] = [item[item_len:]]
    return phone_dict
    
def solution(phone_book):
    answer = True
    # key-> value
    answer = True
    dict_list = []
    for i in range(1,19):
        phone_dict = make_dict(phone_book, i)
        dict_list.append(phone_dict)
        for value in phone_dict.values():
            if len(value) != 1 and '' in value:
                answer=False
                break
    
    
    
    
    ### 효율성 실패
#     answer = True
#     dict1 = {}
#     for item in phone_book:
#         dict1[item] = 
    
#     for k in dict1.keys():
#         for target_k in dict1.keys():
#             if target_k.startswith(k):
#                 if target_k != k :
#                     answer=False
#     print(answer)
    
    ### 정확성 실패
    # phone_book = ["124","1235","567","88"]
#     item_len = find_short_len(phone_book)
#     phone_dict = make_dict(phone_book, item_len)
         
#     print(phone_dict)
    #중복이 발생한 key 구하기
#     key_list = list()
#     for key, value in phone_dict.items():
#         if len(value) != 1 and '' not in value:
#             key_list.append(key)
#     print(key_list)
#     for key in key_list:
#         second_len = find_short_len(phone_dict[key])
#     print(second_len)
#     for key in key_list:
#         phone_dict = make_dict(phone_dict[key], second_len)
#     print(phone_dict)
    
#     key_list = list()
#     for key, value in phone_dict.items():
#         if len(value) != 1 and '' not in value:
#             key_list.append(key)
    
            
    # for item in phone_dict[phone_book_key]:
    #     phone_dict
    
    
        
    
    return answer