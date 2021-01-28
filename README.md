# PythonPractice

(점프투파이썬)[https://wikidocs.net/book/1] 으로 파이썬을 공부 했다

솔직히 그렇게 유익 한 시간이라고 말 할수는 없지만

그래도 파이썬을 자주 사용함에 있어서 유용하게, 자주 쓸만한 것들을 배웠다

그것에 대하여는 여기에 적어 나중에 보러 올 때 여기서 검색용도로 만들었다

나중에 쓸만한 모듈이나 패키지 같은거 있으면 여기에 링크 하자

--------

## 먼저 책에서 배운것 정리


## 1. String = "Python so hard" 

#### 문자열 인덱싱

    String[-1], String[-3] 

#### 문자열 슬라이싱

    String[:], String[2:], String[:5], String[1,5]

#### 문자열 포매팅

    String = "%d %s %.2f" %(1,"2",3.14)
    String = "Python {0} {1} {2}".format(1,2,3)

#### 문자열 정렬

```
"%10s"   왼쪽에 10개의 공백
"%-10s"  오른쪽에 10개의 공백

.format()
{:<10}.format(1)
{:>10}.format(1)
{:^10}.format(1)
{:=^10}.format(1)

f'python {a}'
f'{"py":>10}'  
```

#### 기타 함수들

```
upper(), lower()
strip(), rstrip(), lstrip()  양쪽, 오른쪽, 왼쪽 공백 제거
replace("a to","b")
split(":") ":"를 기준으로 나누기
```


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


## 3. Dict

```python
del dict[key]       # key 찾아서 삭제
dick..keys()        # key 돌려줌
dict.values()       # value 둘려줌
dict.items()        # key와 value의 쌍을 튜플로 묶은 값을 돌려줌
dict.clear()        # key, value 모두 삭제
dict.get(key,default) # key에 해당하는 value 반환, 없으면 defalut(생략가능)

dict in key
```

## 4. Class

```python

#class 사이는 2번 띄우기
class cal():
    def __init__(self):   # 생성자
        self.a = a
        self.b = b
    def add(self):            # 메소드
        return self.a + self.b

class copycal(cal):   # 클래스 상속
    pass

class copycal(cal):    #  메소드 오버라이딩 method overriding
    def add(self):
        return self.a - self.b


a = cal(1,2)
print(a.add())
b = copycal(2,1)
print(b.add()) # 1

# 참고로 메소드 오버로딩은 똑같은 함수를 불러오지만
# 오버라이딩 처럼 재정의가 아닌 매개변수의 유형과 개수를 다르게 하여 사용하는것이다
# 그러니까 클래스 내의 같은 이름의 함수에서 매개변수만 다르게 받는 것```
```

## 5. FileRWA

```python
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
```

## 6. Module

``` python
# mod.py 가 같은 디렉토리에 있다면
import mod
# 를 사용하여 불러올 수 있다.
# 그냥 import 는 a.mod.func() 이렇게 써야함
# 또는 모듈의 함수만 가져오고 싶을 땐
from mod import add
# from을 써서 필요한 함수만 가져 올 수 있다.
from mod import * 
# 로 모든 함수를 가져 올 수 있다.
# from을 쓰면 a.func()로 바로 쓸 수 있음

# 그러나 모듈을 불러오게 된다면
# 클래스의 함수가 아닌 밖의 print와 같은 문장은 바로 실행하게 되는데
if __name__ == "__main__":  
# 를 사용하여 이 아래에 둠으로써 다른 파일에서 실행 시 바로 시작하지 않도록 한다

# sys 모듈을 사용하여 지정한 디렉터리가 사용이 가능하다
import sys
sys.path.append("C:/")
# 이러면 C 안에있는 파이썬 파일이 사용 가능하다

# 또는 PYTHONPATH 환경변수를 사용하는 방법
# cmd 명령어 창에서
# set PYTHONPATH=C:\
# 이러면 C 안에있는 파이썬 파일이 사용 가능하다
```

## 7. Package

# 패키지는 토트 (.)를 사용하여 파이썬의 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다
# 디렉토리가 이렇다고 가정하자
#
C:/doit/gamee/__init__.py
C:/doit/game/sound/__init__.py
C:/doit/game/sound/echo.py
C:/doit/game/graphic/__init__.py
C:/doit/game/graphic/render.py

set PYTHONPATH=C:/doit      # 으로 지정
import game.sound.echo      # 모듈을 import 하는 방법
game.sound.echo.echo_test()

from game.sound import echo # sound까지 들어가서 echo모듈을 불러오는 것
echo.echo_test

from game.sound.echo import echo_test # echo 까지 들어가서 echo_test 함수를 불러옴
echo_test()
# 단 import로 echo_test 함수까지 불러올 수 없다. 오로지 모듈 또는 패키지여야만 한다

# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
# 만약 위의 폴더에서도 __init__.py 파일이 없으면 패키지로 인식하지 않는다.
# 3.3버전부터는 없어도 패키지로 인식 하나 하위버전 호환을 위해 파일 생성하는게 안전하다고 한다

from game.sound import * # 하면 에러가 난다
# __init__.py 파일에 __all__ 변수를 설정하고, import 할 수 있는 모듈을 정의해 주어야 한다
# 예시로는 __init__.py에 __all__ = [‘echo’] 를 넣으면 된다…

from game.sound.game import * # 은 에러가 안남
# 이미 echo 모듈까지 갔기 때문에 echo모듈의 함수들을 불러오기 때문…

# 만약 다른 디렉토리(ex:graphic)에서 sound의 echo.py를 사용하고 싶을 땐
# 위와 동일하다
# graphic의 render.py에
from game.sound.echo import echo_test # 또는
from ..sound.echo import echo_test
# 여기서 (..)은 부모디렉터리를 의마한다
# graphic과 sound는 같은 디렉토리를 사용하므로 (..)를 사용하여 위와 같은 import가 가능하다
# (.) 은 현재 디렉터리, (..)은 부모 디렉터리를 의미한다
