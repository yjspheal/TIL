# 아래 함수를 수정하시오.
def count_character(sentence, char):
    pass
    """
    주어진 문자열에서 특정 문자의 갯수를 세는 함수

    Args:
        sentence (str): 주어진 문자열
        char (str): 특정 문자   

    Returns:
        str: 특정 문자가 들은 갯수
    """

    return sentence.count(char) 


result = count_character("Hello, World!", "o")
print(result)  # 2
