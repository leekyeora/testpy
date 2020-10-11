#변수=poen('경로/파일명', 'w/r/wb/a')
#open함수일때 반드시 close
# r은 읽기보드, w는 쓰기모드, a는 추가모드, r+ 읽기와쓰기모드

file=open('C:\\testpy\\mtest\\day0816\\phone.txt', 'r')
s=file.read() #전체내용읽기
print(s)
#file.write('ezen python \n') #w로 쓰기모드 시
file.close()  #오픈함수는 반드시 close

print('C:\\testpy\\mtest\\day0816\\phone.txt 읽기성공했습니다')