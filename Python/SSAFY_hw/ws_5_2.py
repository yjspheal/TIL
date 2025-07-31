# 아래 함수를 수정하시오.
def remove_duplicates(old_lst):
    """
    주어진 리스트에서 중복된 요소를 제거한 새로운 리스트를 반환하는 함수
    """
    new_lst = []

    for old_element in old_lst:
        if old_element not in new_lst:  # 기존 list에 있던 원소가 new_lst에 없다면
            new_lst.append(old_element)     # new_lst에 추가
        else:                           # new_lst에 들어있다면, 아무것도 하지 않음
            pass
        
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
