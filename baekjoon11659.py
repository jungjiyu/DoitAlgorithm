#
# 문제:
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
#
#문제 분석:
#input:
# 첫번째 줄: 수의 개수 n 과 합을 구해야하는 횟수 m , 띄어쓰기를 구분자로
# 두번째 줄: n 개의 수(대상 배열의 요소들) , 띄어쓰기를 구분자로
# 세번째 줄 "이하": 합을 구해야하는 구간 i 와 j , 띄어쓰기를 구분자로 <- !!!! 주의 : 구간합구하기위해입력하는 인덱스는 0이 아닌 1부터 시작한다
#output: 세번쨰줄 이하 줄에 입력한 구간에 대한 합의 결과 (m회까지 수행 가능)
# 띄어쓰기를 구분자로 -> split()
# 수의 갯수 n -> 대상 배열의 사이즈
# 합을 구해야하는 횟수 m-> 얼마나 추가 입력을 받을 수 있게 할건지 -> for 문
# 여러번 구간합 구해야됨 -> 합배열 사용해 시간복잡도 줄이기


##try1-> 시간초과 나옴
# n,m=map(int,input().split()) # (튜플에 제한된게 아니라) 이터러블 객체이면 언패킹 사용 가능
# print(f"n={n},m={m}")
#
# originList = list(map(int,input().split()))
#
# #합배열 구하기
# sumList=[0]*n # 걍 다짜고짜 개척되지 않는 인덱스에 값 할당한다고 append 되진 않는듯? 확장시에는 append 나 insert 필수적으로 써야되는 것 같다
# sumList[0]=originList[0]
#
# print(f"sumList[0]={sumList[0]}")
# for i in range (n-1): # i = 0~n-1
#     sumList[i+1]=sumList[i]+originList[i+1]
#     print(f"sumList[{i+1}]={sumList[i+1]}")
# print(f"sumList={sumList}")
#
#
# #m번 구간합 구하기
# for k in range(m):
#     i , j =map(int,input().split())
#     i-=1
#     j-=1
#     if(i!=0) :
#         result=sumList[j]-sumList[i-1]
#     else :
#         result = sumList[j] # 0 부터 n 까지의 합 -> sumList[j]-sumList[i-1] 쓰면 안되는게, sumList[-1] 된다
#     print(f"{i}부터{j}까지의 합: {result}")


##try2 -> 시간초과
# n,m=map(int,input().split()) # (튜플에 제한된게 아니라) 이터러블 객체이면 언패킹 사용 가능
# print(f"n={n},m={m}")
#
# originList = list(map(int,input().split()))
#
# #합배열 구하기
# sumList=[]
# sumList.append(originList[0])
#
# print(f"sumList[0]={sumList[0]}")
# for i in range (n-1): # i = 0~n-1
#     sumList.append(sumList[i]+originList[i+1])
#     print(f"sumList[{i+1}]={sumList[i+1]}")
# print(f"sumList={sumList}")
#
#
# #m번 구간합 구하기
# for k in range(m):
#     i , j =map(int,input().split())
#     i-=1
#     j-=1
#     if(i!=0) :
#         result=sumList[j]-sumList[i-1]
#     else :
#         result = sumList[j] # 0 부터 n 까지의 합 -> sumList[j]-sumList[i-1] 쓰면 안되는게, sumList[-1] 된다
#     print(f"{i}부터{j}까지의 합: {result}")


## try3 : (시간초과 원인을 알기 위해) solution 좀 수정한 ver -> 여전히 시간 초과
# n,m=map(int,input().split()) # (튜플에 제한된게 아니라) 이터러블 객체이면 언패킹 사용 가능
# print(f"n={n},m={m}")
#
# originList = list(map(int,input().split()))
#
# #합배열 구하기
# sumList=[0]
# temp =0
#
# print(f"sumList[0]={sumList[0]}")
# for k in originList:
#     temp+=k
#     sumList.append(temp)
# print(f"sumList={sumList}")
#
#
# #m번 구간합 구하기
# for k in range(m):
#     i , j =map(int,input().split())
#     result=sumList[j]-sumList[i-1]
#     print(f"{i}부터{j}까지의 합: {result}")



#solution <- 이건 채점 통과인데 아니 이건 알고리즘 자체보단 템빨 아님??
# from sys import stdin
#
# input = stdin.readline
# n , m = map(int , input().split())
# originList=list(map(int,input().split()))
# sumList = [0]
# temp=0
#
# for k in originList:
#     temp +=k
#     sumList.append(temp)
#
# for k in range(m):
#     i,j=map(int,input().split())
#     print(sumList[j]-sumList[i-1])


## try 4 : 진짜 템빨인지 확인해보기 -> 오 진짜 템빨이 있음 ( 기본 input 안쓰니까 시간 덜걸림)
# from sys import stdin
#
# input = stdin.readline
# n,m=map(int,input().split()) # (튜플에 제한된게 아니라) 이터러블 객체이면 언패킹 사용 가능
# print(f"n={n},m={m}")
#
# originList = list(map(int,input().split()))
#
# #합배열 구하기
# sumList=[]
# sumList.append(originList[0])
#
# print(f"sumList[0]={sumList[0]}")
# for i in range (n-1): # i = 0~n-1
#     sumList.append(sumList[i]+originList[i+1])
#     print(f"sumList[{i+1}]={sumList[i+1]}")
# print(f"sumList={sumList}")
#
#
# ## sol m번 구간합 구하기
# for k in range(m):
#     i , j =map(int,input().split())
#     i-=1
#     j-=1
#     if(i!=0) :
#         result=sumList[j]-sumList[i-1]
#     else :
#         result = sumList[j] # 0 부터 n 까지의 합 -> sumList[j]-sumList[i-1] 쓰면 안되는게, sumList[-1] 된다
#     print(f"{i}부터{j}까지의 합: {result}")


# try5 : 템빨 확인하기2
from sys import stdin,stdout

input = stdin.readline
print = stdout.write

n,m=map(int,input().split()) # (튜플에 제한된게 아니라) 이터러블 객체이면 언패킹 사용 가능
print(f"n={n},m={m}\n")

originList = list(map(int,input().split()))

#합배열 구하기
sumList=[]
sumList.append(originList[0])

print(f"sumList[0]={sumList[0]}\n")
for i in range (n-1): # i = 0~n-1
    sumList.append(sumList[i]+originList[i+1])
    print(f"sumList[{i+1}]={sumList[i+1]}\n")
print(f"sumList={sumList}\n")


#m번 구간합 구하기
for k in range(m):
    i , j =map(int,input().split())
    i-=1
    j-=1
    if(i!=0) :
        result=sumList[j]-sumList[i-1]
    else :
        result = sumList[j] # 0 부터 n 까지의 합 -> sumList[j]-sumList[i-1] 쓰면 안되는게, sumList[-1] 된다
    print(f"{i}부터{j}까지의 합: {result}\n")