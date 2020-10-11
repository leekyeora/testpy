dognames=[]
while True:
    name=input('강아지이름>>> ')
    if name=='': break
    dognames.append(name) #append는 리스트 끝에 추가가능

print()
for name in dognames:
    print(name, end=' ')