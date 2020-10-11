#세트실습, 중복허용x

wish={'bc',2300,'apple',2300,'bc',7800} 
print(wish)
print('-'*80)

#print(wish[0],wish[1]) 이런 형태는 에러발생, 
mywish=list(wish) #그래서 세트를 리스트화 하는방법!
print(mywish[0],mywish[1])