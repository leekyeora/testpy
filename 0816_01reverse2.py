#출력 5942 역순으로 표현
#input으로 받기


#su=int(input('숫자입력>>>'))
#while True:
#    nmg=su%10
#    su=su//10
#    print(nmg, end='')
#    if su==0: break

#매개인자없이 함수출력
def myreverse():
    su=int(input('숫자입력>>> '))
    while True:
        nmg=su%10
        su=su//10
        print(nmg, end='')
        if su==0: break


myreverse()