# PythonPractice

(점프투파이썬)[https://wikidocs.net/book/1] 으로 파이썬을 공부 했다

솔직히 그렇게 유익 한 시간이라고 말 할수는 없지만

그래도 유용하게 쓸 만한 것들은 있다

그것에 대하여는 여기에 적어 나중에 보러 올 때 여기서 검색용도로 만들었다


--------


## 1. String = "Python so hard" 

#### 문자열 인덱싱

String[-1], String[-3] 

#### 문자열 슬라이싱

String[:], String[2:], String[:5], String[1,5]

#### 문자열 포매팅

String = "%d %s %.2f" %(1,"2",3.14)

String = "Python {0} {1} {2}".format(1,2,3)

#### 문자열 정렬


"%10s"   왼쪽에 10개의 공백
"%-10s"  오른쪽에 10개의 공백

.format()
{:<10}.format(1)
{:>10}.format(1)
{:^10}.format(1)
{:=^10}.format(1)

f'python {a}'
f'{"py":>10}'  

#### 기타 함수들

upper(), lower()

strip(), rstrip(), lstrip()  양쪽, 오른쪽, 왼쪽 공백 제거

replace("a to","b")

split(":") ":"를 기준으로 나누기



##
