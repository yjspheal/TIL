# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

# 온라인 저지에서는 stdin 사용 불가하므로 주석처리
# import sys
# sys.stdin = open("sample_input.txt", "r")


def select_charging_station(stations):
    """
    정류장 번호 list를 인자로 받아, 최적의 들를 정류장 조합을 찾아 return하는 함수

    Args:
        stations (list): 각 충전정류장 번호를 원소로 가진 리스트

    Returns:
    """

    # 충전정류장 간의 거리를 계산하여 리스트화
    distances = []
    # to_go_stations = []
    for i in range(1, M + 2):
        distance = stations[i] - stations[i - 1]
        # 거리가 k를 넘는 순간 도달 불가능하므로 바로 0 return.
        if distance > k:
            return 0
        # k라면 해당 정류장은 무조건 가야함 -> 'go' 로 append
        elif distance == k:
            distances.append('go')
        # k
        else:
            distances.append(distance)

    # distances = [1, 2, 'go', 1, 2, 1]

    # distances를 앞에서부터 순회하며, 'go'를 만나기 전까지, 합이 k 이하가 될 때까지 묶음
    idx = 0
    while True:
        # 체크할 idx가 distances의 길이를 넘어버렸다면 break
        if idx >= len(distances):
            break

        # 현재 정류장이 판단이 끝난 상티라면 넘기기
        if distances[idx] == 'go':
            idx += 1
            continue

        # 현재 sum
        current_sum = 0
        for j in range(idx, len(distances)):
            # 만약 'go'를 만났다면 break
            if distances[j] == 'go':
                # 처음 정류장을 go로, j-1까지는 del
                distances = trans_distances(distances, idx, j - 1)
                idx += 1    # 다음 정류장을 볼 수 있게
                break


            # 합 구하기
            current_sum += distances[j]

            # 합이 k를 넘어버렸다면 이 직전까지만 가야함
            if current_sum > k:
                distances = trans_distances(distances, idx, j - 1)
                break

            # k와 같다면 딱 거기까지 가야함
            elif current_sum == k:
                distances = trans_distances(distances, idx, j)
                break

            # k가 안 된다면
            else:
                # 만약 종점까지 다 온 상황이라면
                if j == len(distances)-1:
                    distances = trans_distances(distances, idx, j)
                    break

                # 그게 아니라면 다음정류장으로
                continue

    # 첫 정류장은 충전횟수에 포함하지 않으므로 -1
    return len(distances) - 1


def trans_distances(arr, start_idx, end_idx):
    """
    arr의 start_idx를 'go', start_idx + 1 ~ end_idx까지를 del하여 arr를 반환하는 함수
    """
    arr[start_idx] = 'go'
    del arr[start_idx+1 : end_idx + 1]

    return arr

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # k: 한번 충전으로 이동 가능한 거리(=정류장 수), N: 종점 번호, M: 충전정류장 수
    k, N, M = map(int, input().split())
    # M개의 충전정류장, 출발지, 종점 추가
    station_list = [0] + list(map(int, input().split())) + [N]
    # station_list = [0, 1, 3, 6, 7, 9, 10]

    # 들를 정류장 갯수
    select_station_count = select_charging_station(station_list)

    print(f'#{tc} {select_station_count}')
