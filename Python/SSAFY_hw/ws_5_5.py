# 아래 함수를 수정하시오.
def even_elements(num_list):
    """
    주어진 list에서 홀수를 모두 제거하고 짝수만을 남긴 list를 반환하는 함수
    """

    new_list = []   # 짝수만 담길 리스트 초기화

    # num_list의 모든 원소를 돌며, 홀수라면 pop
    i = 0
    while i < len(num_list):       # pop하면 인덱스가 달라지므로 for d아닌 while
        
        # num_list의 i번쨰 값이 홀수라면 pop
        if num_list[i] % 2 == 1:
            num_list.pop(i)
        
        # 짝수라면 다음 값으로 넘어감
        else:
            i += 1  

    # 홀수가 사라진 리스트를 extend하여 반환
    new_list.extend(num_list)
    return  new_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
