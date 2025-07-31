# 아래 함수를 수정하시오.
def sort_tuple(old_tuple):
    """
    주어진 튜플을 정렬하여 새로운 튜플로 반환하는 함수
    """
    
    new_tuple = ()
    
    # tuple은 immutable이므로 mutable한 자료형으로 변환
    old_list = list(old_tuple)
    
    # old_list 정렬
    old_list.sort()

    # 다시 튜플로 변환
    new_tuple = tuple(old_list)
    
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
