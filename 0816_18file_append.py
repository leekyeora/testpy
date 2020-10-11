import os.path

if os.path.isfile('C:\\testpy\\mtest\\day0816\\phone.txt'):
    #print('C:\\testpy\\mtest\\day0816\\phone.txt 파일이 존재합니다')
    file=open('C:\\testpy\\mtest\\day0816\\phone.txt', 'a')  #a가 append 개념인데 ''이거 필요해
    file.write('coffee \n')
    file.write('baseball 일요일 \n')
    file.close()
else:
    print('C:\\testpy\\mtest\\day0816\\phone.txt 파일이 없어요')

print('C:\\testpy\\mtest\\day0816\\phone.txt 저장성공')