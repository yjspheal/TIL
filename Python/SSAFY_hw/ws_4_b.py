food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]


# 아래에 코드를 작성하시오.

# # for
# for food in food_list:
#     food_name = food["이름"]

#     if food_name == '토마토':
#         food["종류"] = '과일'
#     elif food_name == '자장면':
#         print('자장면엔 고춧가루지')

#     food_type = food["종류"]

#     print(f'{food_name} 은/는 {food_type}(이)다.')

# print(food_list)

# while
i = 0
while i < len(food_list):
    food = food_list[i]

    food_name = food["이름"]

    if food_name == '토마토':
        food["종류"] = '과일'
    elif food_name == '자장면':
        print('자장면엔 고춧가루지')

    food_type = food["종류"]

    print(f'{food_name} 은/는 {food_type}(이)다.')

    i += 1

print(food_list)