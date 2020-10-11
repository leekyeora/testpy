#순서1 def myGtotal(1,2)
#순서2 return 값
#순서3 매개인자(eng, kor) 국어점수, 영어점수
#순서4 매개인자/리턴값은 2개
#함수구현 및 호출, 총점출력 



def myGtotal(kor, eng):
    hap=kor+eng
    return hap

kor=int(input('국어점수 입력>>> '))
eng=int(input('영어점수 입력>>> '))
print('-'*80)
#print('총점은요:', myGtotal(kor,eng))

total=myGtotal(kor,eng) #함수호출
print('총점은? :', total)