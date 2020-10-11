path='C:\\testpy\\mtest\\day0816\\sales.txt'
ret='C:\\testpy\\mtest\\day0816\\summary.txt'


infile=open(path, 'r')
outfile=open(ret, 'w')

#변수정의
salessum=0
linecount=0

for line in infile:
    dailysales=int(line)
    salessum=salessum+dailysales
    linecount=linecount+1

outfile.write('총매출='+str(salessum)+'\n')
outfile.write('평균 일매출='+str(int(salessum/linecount)))

print('summary파일이 저장되었습니다')
infile.close()
outfile.close()