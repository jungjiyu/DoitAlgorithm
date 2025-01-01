# 문제
#     수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
#     즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.
#     입력
#        첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
#        둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)
#     출력
#       첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

# 그러니까 m으로 나눠 떨어지는 구간합 구하고, 그 구간합의 start 와 end 를 구하는 것

#try1

from sys import stdin, stdout
#from time import sleep
input = stdin.readline
print = stdout.write

n,m=map(int,input().split())
originList =list(map(int,input().split()))

#햅배열 구하기, 인덱스 1 부터 유효
sumList=[0] # 완충재
for k in range(1,n+1):
    sumList.append(sumList[k-1] + originList[k-1])
print(f'sumList={sumList}\n')

#합배열 활용 및 나누어떨아지는 인덱스 구하기
total=0
for i in range(1,n+1): # 1<= <= n
    for j in range(i,n+1): # j 는 i 이상이여야
#        sleep(0.5)
        print(f'{i}, {j}\n')
        sectionSum = sumList[j]-sumList[i-1]
        if sectionSum%m==0:
            total+=1
            print(f'{sectionSum}는 {m}으로 나뉘어떨어짐, i : {i}, j:{j}\n')

print(f'total={total}\n')
