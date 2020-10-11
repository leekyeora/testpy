#딕션실습 {}, 키1과 값1이 세트임
#딕셔너리 = {키1:값1, 키2:값2}

#딕션 데이터 추가하기, append, add, insert 아님

ct={'kim':5678,'park':1234,'lee':1519,'shin':2484, 'goo':3400}

#for 반복문으로 딕션의 key,value출력

for item in ct.items(): #딕션의 아이템들을 뽑아와요~
    print(item, end=' ') #튜플처럼 출력한다
print()
print('-'*80)

for a,b in ct.items():
    print(a, ':', b)

print('-'*80)

for c in ct.keys():
    print(c, ':', ct[c]) #ct['lee']=1519 정답

print('-'*80)

for d in ct:
    print(d, ':', ct[d]) #강사추천 딕션출력

print('-'*80)
for e in ct.items(): #튜플처럼 출력
    print(e)

print('-'*80)


