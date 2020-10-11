#세트실습, 중복허용x
#리스트 [ ], 나열순서대로 처리

print('***set은 중복X, 순서없음***') #순서가 있는거 대표적인 것은 리스트이다. 

wish={'bc',2300,'apple',2300,'bc',7800} 
print(wish)
print('-'*80)
#for a in wish:
#    print(a, end=' ')

wish.add('kb국민') #리스트는 추가할때 append/ 셋트는 add
wish.add('bc')
wish.add(7800)
print(wish)