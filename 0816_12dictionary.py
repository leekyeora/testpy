#딕션실습 {}, 키1과 값1이 세트임
#딕셔너리 = {키1:값1, 키2:값2}

contacts={'kim':5678,'part':1234,'lee':1519,'shin':2484}
print(contacts)
print('-'*80)

#print(contacts['kim'])
#print(contacts.get('kim')) #키값을 가져온다

search=input('검색키값 입력>>> ')

if search in contacts:
    print(search,'값: ',contacts.get(search), '존재하네요!')
else:
    print(search,'가 없습니다')