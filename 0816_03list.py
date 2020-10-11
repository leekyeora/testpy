info=[23,91,45,37,6,14,77,59,69]

print(info)
print('-'*80)

for a in info: #리스트출력권장
    print(a, end=' ')

print()
info.sort() #sort는 리스트 정렬! 숫자순
print(info) #쉽게 리스트출력