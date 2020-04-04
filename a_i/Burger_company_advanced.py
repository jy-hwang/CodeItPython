class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


'''
상속을 받는 클래스 Cashier 에서 상속 받은 같은 이름의
메소드를 수정하여 사용해야할 때 오버라이딩

'''


class Cashier(Employee):
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다."""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다.")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name


younghoon = Cashier("강영훈", 8900, 0)

younghoon.raise_pay()
print(younghoon.wage)
print(younghoon.take_order(7000))


class DeliveryMan(Employee):
    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby  # 대기상태

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 설명 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다.")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원을 복귀 처리한다."""
        self.on_standby = True

    pass


taeho = DeliveryMan("성태호", 7000, True)

taeho.raise_pay()
print(taeho.wage)

taeho.deliver("서울시 코드잇로 51 최고 건물 401호")
taeho.deliver("서울시 코드잇로 31 최저 건물 201호")
taeho.back()

print(taeho)
