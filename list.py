
#리스트 연산 - 덧셈, 곱셈,
list1 = ['a','b']
list2 = ['c','d']
list3 = list1+list2 #[ 'a','b','c','d'] -> 이어붙이기
list4 = list1*3 #[ 'a','b','a','b','a','b''] -> n번 이어붙이기
print(f'list3: {list3}')
print(f'list3[-1]: {list3[-1]}')
print(f'list3[-4]: {list3[-4]}')
print(f'list4: {list4}')

#리스트 슬라이싱
list5 = list3[1:3+1] #list[1]~list[3] 까지의 리스트
print(f'list5:{list5}')
list6 = list3[1:] #list[1]~ 까지의 리스트
print(f'list6:{list6}')
list7 = list3[:2+1] #~list[2] 까지의 리스트
print(f'list7:{list7}')


#내장함수 활용
print(f'len(list3):{len(list3)}')
del(list3[1:2+1])
print(f'list3 after del(list3[1:2+1]):{list3}')

#list 메서드 활용
listA = [1,2,3,4,5]
print(f'listA:{listA}')
listA.append(7)
print(f'listA after append :{listA}') #제일 끝에 추가
listA.insert(5,6)
print(f'listA after insert :{listA}') #특정 위치 추가

listB=['a','b','c']
listA.extend(listB)
print(f'listA after listA.extend(listB) : {listA}')

listA.remove('c')
print(f'listA after listA.remove("c") : {listA}')

del(listA[7:])
listA.reverse()
print(f'listA after listA.reverse() : {listA}')
listA.sort()
print(f'listA after listA.sort() : {listA}')

listC = listA # 얕은 복사
listD = listA.copy() # 깊은 복사
print(f'listA: {listA }, listC: {listC}, listD: {listD}')
listC.remove(1)
print(f'after listC.remove(1) -> listA: {listA }, listC: {listC}, listD: {listD}')


## 개척되지 않은 인덱스를 인덱스 통해 바로 append 가능?
# 불가하다
# Traceback (most recent call last):
#   File "C:\Backend\doitAlgorithm\pythonBasic\list.py", line 56, in <module>
#     listAA[1]=2
#     ~~~~~~^^^
# IndexError: list assignment index out of range

listAA = [0]
listAA.append(2)#listAA[1]=2 하면 에러남
print(listAA)
