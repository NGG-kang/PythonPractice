# Dictionary

# 딕셔너리는 key와 value를 가진다
a = {1:'a'}                 # 여기서 1은 key 'a'는 value이다
a = {1:[a,b,c]}             # 딕셔너리 안에 리스트도 가능하다

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
{1: 'a', 2: 'b'}
{1: 'a'}
# 딕셔너리에 a[2] = 'b'와 같이 입력하면
# 딕셔너리 a에 Key와 Value가 각각 2와 'b'인 2 : 'b'라는 딕셔너리 쌍이 추가된다.

a['name'] = 'pey'
{1: 'a', 2: 'b', 'name': 'pey'}
# 딕셔너리 a에 'name': 'pey'라는 쌍이 추가되었다.
a[3] = [1,2,3]
{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔러니 요소 삭제하기
del a[key]
del a[1]
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# key를 사용해 value 얻기
a[2]                        # b
a['name']                   # 'pey'

# 딕셔너리 주의사항
# 중복되는 key값을 설정하면 하나를 제외한 나머지는 모두 무시
# key에는 list를 쓸 수 없다, 쓰면 오류남

# 딕셔너리 관련 함수들
# a.keys()는 딕셔너리 a의 key만 모아서 dick_keys 객체를 돌려준다
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
dict_keys(['name', 'phone', 'birth'])
# dict_keys 객체를 리스트로 변환하려면 list(a.keys())를 사용하면 된다
list(a.keys())

a.values()                  # 딕셔너리 a의 value만 모아서 dict_values를 반환한다
a.items()                   # 는 딕셔너리의 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다

a.clear()                   # key: Value 쌍 모두 지우기

# key로 value 얻기(get)
a.get('name') / 'pey'
# 만약 get에서 키값이 없는거라면 None을 반환한다
# a.get(x, default) 를 사용하면 x가 없을 시 디폴트 값을 반환한다

# 해당 key가 딕셔너리에 있는지 조사하기 (in)
'name' in a  # True
'aa' in a # False