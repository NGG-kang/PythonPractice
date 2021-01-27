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



## 2. List

문자열과 동일하게 슬라이싱이 가능하다

del [1:]

#### 기타 함수
```python
a.sort()               # 리스트 요소 순서대로 정렬, 문자열도 알파벳 순서
a.reverse()            # 리스트를 역순으로 뒤집음, 정렬후 역순이 아닌 그냥 뒤집는것
                       # 단 sort나 reverse는 print로 안나온다, 값을 다른 곳에 저장해야함
a.index(x)             # 리스트 x에 값이 있으면 x의 위치값을 돌려줌, 없으면 오류
a.append(4)            # 리스트 뒤에 요소 추가
a.insert(0,x)          # 0번방에 x이라는 값을 넣는다, 넣은 다음 뒤의 값들은 뒤로 밀린다
a.remove(x)            # 리스트에서 첫 번째로 나오는 x를 삭제하는 함수
a.pop()                # 리스트의 맨 마지막 요소를 돌려주고, 삭제한다 / pop에 x를 넣으면 x번째 요소를 돌려주고, 삭제한다
                       # 그러니까 pop은 방 번호로 삭제, remove는 요소의 값을 찾아서 삭제
a.count(x)             # 리스트에서 x의 개수를 돌려줌
a.extend([a,b])        # a리스트에서 [a,b]를 더한다 // 그냥 리스트 더하기랑 같다...
```
