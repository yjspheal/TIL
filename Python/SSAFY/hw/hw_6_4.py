# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, k, v):
    """
    주어진 딕셔너리에서 특정 키와 값을 이용하여 항목을 추가하는 함수

    Args:
        dictionary (dict): 주어진 딕셔너리
        k (str):  추가할 키
        v (str): 추가할 값

    Returns:
        dict: dct에서 항목이 추가된 딕셔너리
    """
    new_dict = dictionary.copy()

    # 항목을 추가
    new_dict[k] = v

    # 딕셔너리 반환
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
