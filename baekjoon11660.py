
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


##try1 -> 시간 제한에서 걸림 ㅋ
from sys import stdin,stdout

input = stdin.readline
output = stdout.write

n,m= map(int,input().split())
print(f'n={n}, m={m}\n')
#2차원 리스트 생성 -> 일단 [] 으로 초기화해보자
originList =[]
for k in range(n):
    originRow = list(map(int, input().split()))
    originList.append(originRow)
    print(f'originRow={originRow}, originList={originList}\n')
print(f'final originList={originList}\n')


# 2차원 리스트 대한 합 배열 생성, 인덱스는 1 부터 시작하게 하기
sumList=[0]
for i in range(n):
    sumRow=[0] # 인덱스 0 은 완충제 역할, 1~n 에 유효값 저장
    temp = 0
    for j in range(n):
        temp = sumRow[j]+ originList[i][j]
        sumRow.append(temp)
        print(f'temp={temp}, sumRow={sumRow}\n')
    sumList.append(sumRow)
    print(f'sumRow={sumRow}, sumList={sumList}\n')
print(f'final sumList={sumList}\n')

# 구간합 구하기
for k in range(m):
    x1,y1,x2,y2=map(int, input().split())
    print(f'x1={x1},y1={y1},x2={x2},y2={y2}')
    result=0
    for i in range(x1,x2+1):
        result+=(sumList[i][y2]-sumList[i][y1-1])
        print(f"result={result}")
    print(f'final result = {result}')


