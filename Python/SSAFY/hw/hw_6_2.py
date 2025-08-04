# 아래 함수를 수정하시오.
def remove_duplicates_to_set(lst):
    """
    주어진 리스트에서 중복된 요소를 제거한 후, set으로 변환하는 함수
    
    Args:
        lst (list): 주어진 리스트

    Returns:
        set: 중복이 제거된 set
    
    """
    
    unique_ele = set()
    
    # set에 하나씩 추가함으로서 중복된 요소를 제거
    for element in lst:
        unique_ele.add(element)

    return unique_ele


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
