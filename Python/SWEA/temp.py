# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

# import sys
# sys.stdin = open("sample_input.txt", "r")

# + [code]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    card_strs = input()

    card_count = [0] * 10
    for card_str in card_strs:
        card_count[int(card_str)] += 1

    max_card_count = max(card_count)
    card_count = card_count[::-1]
    inverse_max_card_num = card_count.index(max_card_count)
    max_card_num = 9 - inverse_max_card_num

    print(f'#{test_case} {max_card_num} {max_card_count}')

# + [markdown]
# ## 📌 총평
# - 문제 요구사항을 정확히 이해하고, 카드 개수를 세어 최댓값과 대응되는 숫자를 찾는 로직이 올바르게 구현되었습니다.  
# - 입력된 문자열을 뒤집어 처리한 뒤 인덱싱으로 원래 값을 도출하는 방식으로, 카드 번호가 동일할 때 큰 숫자를 우선 처리한 점이 논리적으로 타당합니다.

# ## 🛠 보완점
# ### 1. 커스텀 key를 사용한 max 함수 활용
# `max(range(10), key=lambda x: (card_count[x], x))`를 사용하면 역순 처리 없이 깔끔하게 최댓값을 구할 수 있음

# ### 2. 변수명 및 반복문 간소화
# - `card_strs` → `cards`
# - `for card in input():` 형태로 축소 가능

# ## ✅ 최종 코드 예시
# ```python
# T = int(input())
# for test_case in range(1, T + 1):
#     input()
#     card_count = [0] * 10
#     for card in input():
#         card_count[int(card)] += 1
#     max_card_num = max(range(10), key=lambda x: (card_count[x], x))
#     print(f'#{test_case} {max_card_num} {card_count[max_card_num]}')
# ```
