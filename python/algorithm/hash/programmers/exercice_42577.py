## https://school.programmers.co.kr/learn/courses/30/lessons/42577

#phone_book = ["119", "97674223", "1195524421"]
#phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]

def solution(phoneBook):
    phoneBook.sort() ## 먼저 오름차순으로 정렬하고나서
    i = 1
    while i < len(phoneBook):
        if phoneBook[i].startswith(phoneBook[i-1]):
            return False
        i += 1 ## 한칸씩 추가해가며 startswith 함수로 비교하기!
    return True

print(solution(phone_book))
