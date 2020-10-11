#site={} #딕션을 선언해서 naver, daum, python

#naver : www.naver.com
#daum : www.daum.net
#python : www.python.org

#딕션에서 키값이 문자일 경우 무조건 ''해야함

print('-'*80)
site={'naver':'www.naver.com', 'daum':'www.daum.net', 'python':'www.python.org'}
search=input('naver, daum, python 중에 사이트이름 넣어보렴>>> ')

for i in site:
    if search==i:
        print(search,' : ',site[i])

print('-'*80)

site2={}
site2['naver2']='www.naver.com'
site2['daum2']='www.daum.net'
site2['python2']='www.python.org'

for my in site2:
    print(my, ':', site2[my])


