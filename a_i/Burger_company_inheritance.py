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


class Cashier(Employee):
    pass


younghoon = Cashier("강영훈", 8900)

younghoon.raise_pay()
print(younghoon.wage)
print(younghoon)


# help(Cashier)

class DeliveryMan(Employee):
    pass


jiwoong = DeliveryMan("최지웅", 7000)
jiwoong.raise_pay()
print(jiwoong.wage)
print(jiwoong)

print(Cashier.mro())

print(isinstance(younghoon, Cashier))
print(isinstance(jiwoong, Cashier))
print(isinstance(jiwoong, Employee))

print(issubclass(Cashier, Employee))
print(issubclass(Cashier, object))
print(issubclass(DeliveryMan, Employee))
print(issubclass(Employee, list))
