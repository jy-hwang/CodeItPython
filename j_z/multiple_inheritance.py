# 엔지니어 클래스
class Engineer:
    def __init__(self, favorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print("{}(으)로 프로그래밍합니다.".format(self.favorite_language))


# 테니스 선수 클래스
class TennisPlayer:
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level

    def play_tennis(self):
        print("{} 반에서 테니스를 칩니다.".format(self.tennis_level))


captain = Engineer("자바스크립트")
yoonsoo = TennisPlayer("초급")

# 각 클래스가 잘 작동하는 지 확인

captain.program()
yoonsoo.play_tennis()
