# 100만 * 100만을 방지하기 위해서 hash를 이용함
# 100만 * 최대 길이 20을 탐색하는게 빠를것이라고 생각함
# 꼭 길이가 아니고 알파벳 순 sort를 사용해서 다음 원소들과 비교하는 방법도 있었음

# simple answer -> 문자열순 정렬한 다음 다음 단어랑만 비교함 딱 100만번 돌고 끝일듯?
# 다음 단어와 비교하는 방식 코드 모양 기억해두자.
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

#내꺼
def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x : len(x))
    phone_dict = {}
    first_len = len(phone_book[0])
    for phone in phone_book:
        tmp = phone[:first_len]
        if len(phone) == first_len:
            phone_dict[phone] = True
        else :
            for char in phone[first_len:]:
                if tmp in phone_dict:
                    return False
                tmp += char
                
            phone_dict[phone] = True
    return True