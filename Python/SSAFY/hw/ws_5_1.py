# 아래 함수를 수정하시오.
def reverse_string(sentence):
    """
    주어진 문자열을 역순으로 변환하여 반환합니다.

    Args:
        sentence (str): 뒤집을 대상 문자열.

    Returns:
        str: 입력 문자열을 뒤집은 결과 문자열.
    """
    
    # reversed만 하면 reversed iterator를 반환 -> list로 풀어주기
    reversed_sentence_list = list(reversed(sentence))
    # join으로 하나의 문자열로 묶어주기
    reversed_sentence = ''.join(reversed_sentence_list)

    return reversed_sentence


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
