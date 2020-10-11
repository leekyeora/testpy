#딕션실습 {}, 키1과 값1이 세트임
#딕셔너리 = {키1:값1, 키2:값2}

#딕션 데이터 추가하기, append, add, insert 아님

contacts={'kim':5678,'park':1234,'lee':1519,'shin':2484}
contacts['goo']=3400 #contacts[키]=value
contacts['shin']=3400 #키값이 중복일 경우, 덮어씌워버림
contacts['LG']=3212
contacts.pop('park')

print(contacts)
