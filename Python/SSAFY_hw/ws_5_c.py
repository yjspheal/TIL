def restructure_word(word, arr):
    '''
    주어진 word 문자열을 한 글자씩 순회하며 arr 리스트에서 불필요한 요소를 제거한 후,
    최종적으로 재구성된 리스트를 반환합니다.

    Args:
        word (str): 제거 기준이 되는 문자열.
            - 숫자인 문자는 해당 숫자만큼 arr의 마지막 요소를 pop 합니다.
            - 숫자가 아닌 문자는 해당 문자를 arr에서 remove 합니다.
        arr (list): 요소 제거 대상이 되는 리스트. 함수 실행 중 직접 변경(mutate)됩니다.

    Returns:
        list: word 기준에 따라 요소가 제거된 arr 리스트.

    Raises:
        ValueError: arr에 존재하지 않는 문자를 remove 하려 할 때 발생할 수 있습니다.
        IndexError: pop할 요소가 부족한 상태에서 숫자만큼 pop을 시도할 때 발생할 수 있습니다.

    Examples:
        >>> restructure_word('2ab', ['a', 'b', 'c', 'd', 'e'])
        ['a', 'b']
        >>> restructure_word('3c', ['c', 'c', 'c', 'd'])
        []
    
    Note:
        - arr 리스트를 직접 수정하므로, 원본을 보존하려면 호출 전에 복사하세요.

    '''
    
    for invalid_char in word:
        if invalid_char.isdecimal():            # 순회중인 문자열이 숫자라면
            for _ in range(int(invalid_char)):  # 해당 숫자만큼 arr의 마지막 요소를 제거한다    
                arr.pop()                           
        else:                                   # 그 외의 경우라면
            arr.remove(invalid_char)            # 해당 문자열을 제거한다.

    return arr  # arr 반환
    

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

# original_word를 모두 분리하여 arr에 extend 후 arr 출력
arr.extend(list(original_word))
print(arr) 

# 이상한 문자 제거된 문자열 result에 할당
result = restructure_word(word, arr)
print(result)

# join하여 다시 출력
print(''.join(result))