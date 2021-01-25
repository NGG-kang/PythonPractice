# for문

for 변수 in 리스트(또는 튜플, 문자열):
# 리스트 넣을 시 변수에는 리스트의 요소가 들어간다
for i in range(5):         # 5까지
for i in range(1,5):       # 1부터 5까지
for i in range(5,0, -1):   # 5부터 0까지 -1씩 까짐

# 리스트 내 포 사용하기
# 이건 좀 기니까 예시로 대체
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

# for문을
result = [n*2 for n in numbers if n%2 == 1]
# 로 대체한다
