class Citizen:
    """주민 클래스"""
    '''
    property 데코레이터 사용
    변수의 직접 사용을 최소화 할 수록
    유지 보수가 용이한 소스코드가 된다.
    '''
    drinking_age = 19

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.age = age
        self.resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 확인하는 메소드"""
        return self.name + "씨는 " + str(self.age) + " 살 입니다!"

    '''
    property 데코레이터 : 변수의 값을 읽거나 설정하는 부분
    -> 아예 다른 의미로 실행됨.
    '''

    @property
    def age(self):
        print("나이를 리턴합니다.")
        return self._age

    @age.setter
    def age(self, value):
        print("나이를 설정합니다.")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0 으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value


kyusik = Citizen("최규식", 25, "12345678")
print(kyusik.age)
