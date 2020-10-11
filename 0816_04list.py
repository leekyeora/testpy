list1=list() #이런 형태의 함수도 가능
list2=list("Hello")
list3=list(range(0,5))

print(list1)
print(list2)
print(list3)
print()

list22=[['seoul',10],['paris',12],['london',59]]
print(list22)

print('-'*80)
flist=['apple','banana','tomato','peach','pear']
print(flist[0], flist[2], flist[-1]) #-1은 뒤에서부터 가지고오고 싶을때
print('-'*80)

squares=[0,1,4,9,16,25,36,49]
print( 'squares',squares[3:6]) #3~5까지 나옴, 리스트는 0부터 시작