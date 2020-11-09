class Ship:
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        """연료량, 시간당 연료 소비량, 물자량, 선원 수를 인스턴스 변수로 갖는다"""
        self.fuel_tank = FuelTank(fuel)
        self.crew_manager = CrewManager(num_crew)
        self.supply_hold = SupplyHold(supplies, self.crew_manager)
        self.engine = Engine(self.fuel_tank, fuel_per_hour)


class FuelTank:
    """연료 탱크 클래스"""

    def __init__(self, fuel):
        """연료 탱크에 저장된 연료량을 인스턴스 변수로 갖는다"""
        self.fuel = fuel

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def use_fuel(self, amount):
        """연료 사용 메소드"""
        if self.fuel - amount >= 0:
            self.fuel -= amount
            return True
        print("연료가 부족합니다")
        return False

    def report_fuel(self):
        """연료량 보고 메소드"""
        print("현재 연료는 {}l 남아 있습니다.".format(self.fuel))


class Engine:
    """엔진 클래스"""

    def __init__(self, fuel_tank, fuel_per_hour):
        """연료 탱크 인스턴스와 시간당 연료 소비량을 인스턴스 변수로 갖는다."""
        self.fuel_tank = fuel_tank
        self.fuel_per_hour = fuel_per_hour

    def run_engine_for_hours(self, hours):
        """엔진 작동 메소드,연료 탱크 인스턴스를 사용한다."""
        if self.fuel_tank.use_fuel(self.fuel_per_hour * hours):
            print("엔진을 {}시간 동안 돌립니다".format(hours))
            return True
        print("연료가 부족하기 때문에 엔진 작동을 시작할 수 없습니다.")
        return False


class CrewManager:
    """선원 관리 클래스"""

    def __init__(self, num_crew):
        self.num_crew = num_crew

    def report_crew(self):
        """선원 수 보고 메소드"""
        print("현재 선원 {}명이 있습니다.".format(self.num_crew))

    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number


class SupplyHold:
    """물자 창고 클래스"""

    def __init__(self, supplies, crew_manager):
        """물자량과 선원 관리 인스턴스를 인스턴스 변수를 갖는다"""
        self.supplies = supplies
        self.crew_manager = crew_manager

    def report_supplies(self):
        """물자량 보고"""
        print("현재 물자는 {}명분이 남아 있습니다.".format(self.supllies))

    def load_supplies(self, amount):
        """물자 보급 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자량 배분 메소드"""
        if self.supplies >= self.crew_manager.num_crew:
            self.supplies -= self.crew_manager.num_crew
            return True
        print("물자가 부족하기 때문에 배분할 수 없습니다.")
        return False
