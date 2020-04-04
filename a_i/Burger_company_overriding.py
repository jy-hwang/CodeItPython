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
    '''
    def __init__(self, name, wage, number_sold):
        self.name = name
        self.wage = wage
        self.number_sold = number_sold
    '''
    '''
    def __init__(self, name, wage, number_sold):
        Employee.__init__(self, name, wage)
        self.number_sold = number_sold
    '''

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name


younghoon = Cashier("강영훈", 8900, 0)

younghoon.raise_pay()
print(younghoon.wage)
print(younghoon)


# help(Cashier)

class DeliveryMan(Employee):
    pass
