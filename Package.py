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
