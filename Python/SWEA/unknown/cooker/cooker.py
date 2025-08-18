# [모의 SW 역량테스트] 요리사

"""
식재료 N개를 반띵하여, 최대한 비슷한 맛이 나는 요리를 만들자
"""
import sys
sys.stdin = open('sample_input(1).txt')

T = int(input())
for tc in range(1, T + 1):

    print(f'#{tc} ')