colors=['red','yellow','green','blue','orange','purple','while','black']
print(colors) #전체출력

key=input('원하는 색 검색>> ')

#리스트에 있는지 검색하는 요소, in 연산자 사용

if key in colors:
    print(key, '컬러가 있습니다')
else:
    print(key, '컬러가 없습니다')

#index
print('-'*80)
print('11:31 리스트실습')
print('-'*80)

position=colors.index('blue') #colors 리스트에 있는 blue의 위치를 찾아 position에 넣어줌
print('blue위치는?',position,'입니다')

print('-'*80)

try:
    position2=colors.index(key) #내가 검색하는 컬러의 위치가 나온다, 없는 데이터가 있으면 에러발생함
    print(key,'위치는?',position2,'입니다')
except:             #에러이유 설명해주는 방법     >>>  except Exception as ex: print('에러이유', ex)
    pass

print('-'*80)
colors.pop(0) #0빠짐
colors.pop(1) #0이 빠지면 순서바뀜
colors.remove('blue') #이름데이터로 삭제
for a in colors:
    print(a, end=' ')