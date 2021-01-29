# mod.py 가 같은 디렉토리에 있다면
import mod # 를 사용하여 불러올 수 있다.
# 그냥 import 는 a.mod.func() 이렇게 써야함
# 또는 모듈의 함수만 가져오고 싶을 땐
from mod import add
# from을 써서 필요한 함수만 가져 올 수 있다.
from mod import * # 로 모든 함수를 가져 올 수 있다.
# from을 쓰면 a.func()로 바로 쓸 수 있음

# 그러나 모듈을 불러오게 된다면
# 클래스의 함수가 아닌 밖의 print와 같은 문장은 바로 실행하게 되는데
if __name__ == "__main__":  # 를 사용하여 이 아래에 둠으로써 다른 파일에서 실행 시 바로 시작하지 않도록 한다

# sys 모듈을 사용하여 지정한 디렉터리가 사용이 가능하다
import sys
sys.path.append("C:/")
# 이러면 C 안에있는 파이썬 파일이 사용 가능하다

# 또는 PYTHONPATH 환경변수를 사용하는 방법
# cmd 명령어 창에서
# set PYTHONPATH=C:\
# 이러면 C 안에있는 파이썬 파일이 사용 가능하다
