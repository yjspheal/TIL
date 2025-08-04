# 아래 함수를 수정하시오.
def capitalize_words(sentence):
    """
    주어진 문자열에서 모든 단어의 첫글자를 대문자로 변경하는 함수
    """
    pass

    titled_words = []

    for word in sentence.split():   # sentence를 단어화
        titled_words.append(word.title())   # 첫글자 대문자로 하여 titled_words에 추가

    return ' '.join(titled_words)   # 공백으로 연결하여 문자열로 반환


result = capitalize_words("hello, world!")
print(result)
