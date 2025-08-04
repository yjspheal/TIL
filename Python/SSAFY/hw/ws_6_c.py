data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

# data를 순회하여 얻은 dict를
for dict in data:
    # key_list를 순회하며 얻은 값에 따라
    for key in key_list:
        # 만약 순회중인 dict에 key가 없다면 해당 key에 unknown 문자열을 할당한다
        # get과 setdefault 활용
        dict.setdefault(key, 'unknown')

        # 모든 상황에 대해 key는 value입니다를 출력한다.
        print(f'{key}는 {dict.get(key)}입니다.')

    print()