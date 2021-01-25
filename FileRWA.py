#File 읽기 쓰기 수정

f = open('test.txt','w')        # 파일을 새로 만들어서 쓴다, 덮어쓰기로 가능
f.write('파일 쓰기')

f = open('test.txt','r')
f.readline()                    # 한 줄 읽기
f.readlines()                   # 한 줄씩, 리스트 형태로 읽기
f.read()                        # 파일 내용 전체를 문자열로

f = open('test.txt','a')
f.write('기존 파일 그대로, 이어서 쓰기')

f.close()                       # 사용하면 닫아줘야 다음 파일 사용시 에러가 없다
                                # with문을 사용하면 자동으로 해줌

with open('test..txt', 'w') as f:
     f.write('텍스트')
