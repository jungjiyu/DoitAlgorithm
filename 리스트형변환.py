listA =[1,2,3,4,5]
listB = list(listA) # 다른 리스트를 인자로 하여 해당 리스트의 요소를 요소로하는 리스트 새로 생성
print(listA)
listC = list((map(chr, list(listA))))
print(listC)
listD = list("ABCDE") #결론적으로 list( 이터러블객체 )
print(listD)