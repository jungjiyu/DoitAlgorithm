
#문제:
# N×N개의 수가 N×N 크기의 표에 채워져 있다.
# (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

#문제분석
#입력
#   첫째줄 : 행렬의 사이즈 n , 합을 구할 횟수 m
#   두번째줄 이후 n 개의 줄 : 행렬의 각 행 원소들, 띄어쓰기를 구분자로
#   이후 m 개의 줄 : 합 구할 좌표 범위 x1 y1 x2 y2, 띄어쓰기를 구분자로
#출력
#   m 개의 합 질의에 대한 결과
#구현 계획
# NxN 행렬 -> NxN 2차원 배열(리스트) -> 초기하 어케할까?? 이차원배열??
# 띄어쓰기 구분자 -> .split()
# 2차원 배열에서 구간합 구하기 :
#   일단 합배열은 행 단위로 생성해두고, x2-x1 으로 어떤 행에 대해 실행할지, y2-y1으로 각 행의 어떤 인덱스 범위로 구할지 정함 될 듯


##try1
from sys import stdin,stdout
from time import sleep

input = stdin.readline
output = stdout.write

n,m= map(int,input().split())
print(f'n={n}, m={m}\n')
#2차원 리스트 생성 -> 일단 [] 으로 초기화해보자
originList =[]
for k in range(n):
    originRow = list(map(int, input().split()))
    originList.append(originRow) # append 로 단순 값 뿐 아니라 list 단위도 추가 가능하다
    print(f'originRow={originRow}, originList={originList}\n')
print(f'final originList={originList}\n')


# 2차원 리스트 대한 합 배열 생성, 인덱스는 1 부터 시작하게 하기
# 주의 : sumList[i][j] == originList[0][0] ~ originList[i][j] 영역 값들의 합인거지, originList의 i 행의 일차원 리스트에서 j 번째 원소까지의 합을 말하는게 아니다
tempRowList=[0]*(n)
sumList=[]
sleep(1) # 초 단위. <- 이거 안쓰면 f'{sumList[0][0]} ' 가 출력되기도 전에 다음 코드에 대한 에러가 출력되어 헷갈려서 좀 기다리게 함

for i in range(n): # 미리 초기화. 존재하지 않는 인덱스 접근시 발생하는 에러 방지 차원에서.
    tempRowList = [0] * (n)
    sumList.append(tempRowList)

print(f'init sumList = {sumList} ')

sumList[0][0]=originList[0][0]

# 첫 row , col 초기화
for k in range(1,n):
    sumList[0][k]=sumList[0][k-1] + originList[0][k]
    sumList[k][0]=sumList[k-1][0] + originList[k][0]

print(f'init sumList2 = {sumList} ')

# 내부 초기화
for i in range(1, n):
    for j in range(1, n):
        sumList[i][j] = sumList[i - 1][j] + sumList[i][j - 1] + originList[i][j] - sumList[i - 1][j - 1]
        print(f'sumList={sumList}\n')

print(f'final sumList={sumList}\n')

# 구간합 구하기
for k in range(m):
    x1,y1,x2,y2=map(int, input().split())
    print(f'input : x1={x1},y1={y1},x2={x2},y2={y2}')
    x1-=1
    x2-=1
    y1-=1
    y2-=1
    print(f'내부적 수정 : x1={x1},y1={y1},x2={x2},y2={y2}')
    result = sumList[x2][y2]
    subRowIdx=x1-1
    subColIdx=y1-1
    if(subRowIdx>=0):
        result-=sumList[subRowIdx][y2]
        print(f"첫 if, 현 result ={result}")

    if(subColIdx>=0):
        result-=sumList[x2][subColIdx]
        print(f"두번쨰 if, 현 result ={result}")

        if subRowIdx >= 0 :
            result+=sumList[subRowIdx][subColIdx]
            print(f"세번쨰 if, 현 result ={result}")

    print(f"result={result}")


##solution
# 문제 조건 상 질의 갯수 최대 100,000 으로 질의마다 합을 구하면 ㅈ되는거고 구간 합 배열을 써야된다
# 이 문제의 핵심은 원본배열이 2차원이기에 구간 합 배열도 1차원이 아닌 2차원이라는 것
# 2차원 구간 합 배열을 정의 :  sumList[i][j] == originList의 [0][0] ~ [i][j] 까지의 영역 안에 있는 수의 sum 을 원소로 하는 배열

