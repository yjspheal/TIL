# WIT : What I Think
 
# 1. start_point, end_point 확인
# -> 가본 값에 start_point를 append
# 2. 주변에 0값을 확인 -> 0_list
# 3. 안 가본 값이라면 일단 가.
# 4. 가본 값 밖에 없다면 프로그램 종료, return 0
# 5. 갔다가 end_point에 도착했다면 종료, return 1
 
 
def where_to_go(now_point):
 
##### 이동 가능한 점은 row가 같을 때 col +-1   / col이 같을 때 row +-1
     
    ### 간축버전 < - 으로 하면 왜 안 대
     
    '''x,y = now_point
 
    can_go = [(x, y+1), (x,y-1), (x+1,y), (x-1, y)]
     
    really_can_go = []
    for tu in can_go:
        x,y = tu
        if x>=0 and x< array_size:  # x 통과
            if y>=0 and y<array_size:
                if tu not in went_point:
                    if tu not in no_point:
                        really_can_go.append((x,y))
    can_go = really_can_go
    '''
     
    ### 설명 버전
     
    x, y = now_point
 
    # 이론상 갈 수 있는 점은 위 아래 왼쪽 오른쪽
    can_go = [(x, y+1), (x,y-1), (x+1,y), (x-1, y)]
 
    # 진짜 갈 수 있는지 검사해야해
    # 1. n*n 행렬 안에 있는 값이니?
    really_can_go = []
    for tu in can_go:
        x,y = tu
        if x>=0 and x< array_size:  # x 통과
            if y>=0 and y<array_size:
                really_can_go.append((x,y))
    can_go = really_can_go
 
    # 2. 직전에 머물던 점이면 안 돼
    really_really_can_go = []
    for tu in can_go:
        if tu not in went_point:
            really_really_can_go.append(tu)
    can_go = really_really_can_go
                     
 
    #3. 벽이면 안 돼
    really_really_really_can_go = []
    for tu in can_go:
        if tu not in no_point:
            really_really_really_can_go.append(tu)
    can_go = really_really_really_can_go
 
    #print(can_go)
 
    return can_go
     
 
 
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    array_size = int(input())   #n*n 행렬에서 n값 확인
    array_list = []                 # n*n행렬 담을 리스트
    for a in range(array_size):  # 각 줄마다 받아와서 array_list에 추가할거야
        i = list(map(int, input()))   
        array_list.append(i)
    #print(array_list)
    # [[1, 3, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 2, 1]]
     
     
     
    ########### 행렬 input 받아서,
    ############ 시작점, 도착점, 길, ~길 구분하는 코드입니다.
     
    no_point = [] #벽
    yes_point = [] #길
    went_point = [] #다녀간 길
        
    for row in range(array_size):
        for col in range(array_size):
            if array_list[row][col] == 2:    #출발
                start_point = (row,col)
            elif array_list[row][col] == 3:  #도착
                end_point = (row, col)
            elif array_list[row][col] == 1:   # 벽
                no_point.append((row, col))
            else:                             # 길 
                yes_point.append((row,col))
    #print(start_point)         # (4,3)
    #print(end_point)          # (0,1)
    #print(yes_point)          # [(0, 3), (1, 1), (1, 3), (2, 1), (2, 3), (3, 1), (3, 3), (4, 1), (4, 2)]
    #print(no_point)          # [(0, 0), (0, 2), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 4), (3, 0), (3, 2), (3, 4), (4,   ...
 
     
 
     
 
 
 
    #출발점에서 시작해볼까...
    now_point = start_point
 
 
    num_where_to_go = len(where_to_go(now_point)) # 갈 곳의 개수
    while num_where_to_go != 0:   # 갈 곳 있다면,
        went_point.append(now_point)
        if num_where_to_go >1: # 한 곳 이상이라면,
            while num_where_to_go !=0:
                now_point = where_to_go(now_point)[0]
                went_point.append(now_point)
                if now_point == end_point:
                    print(f'#{test_case} 1')  #도착
                    break
            while num_where_to_go !=0:
                now_point = where_to_go(now_point)[1]
                went_point.append(now_point)
                if now_point == end_point:
                    print(f'#{test_case} 1')  #도착
                    break
 
        else: # 갈 곳이 하나 뿐이라면
            now_point = where_to_go(now_point)[0]
            went_point.append(now_point)
            if now_point == end_point:
                print(f'#{test_case} 1')  #도착
                break
 
    if now_point == end_point:
        print(f'#{test_case} 1')  #도착
 
    else:
        print(f'#{test_case} 0')