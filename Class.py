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
# 그러니까 클래스 내의 같은 이름의 함수에서 매개변수만 다르게 받는 것
