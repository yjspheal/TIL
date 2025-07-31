# 아래 함수를 수정하시오.
def find_min_max(nums):
    '''
    주어진 리스트에서 최솟값과 최댓값을 찾는 함수
    
    Args:
        nums (list): 최소, 최댓값을 찾을 리스트
    
    Returns:
        tuple: (최소값, 최댓값)
        
    '''

    return min(nums), max(nums)

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
