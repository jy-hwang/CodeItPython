class User:
    def say_hello(some_user):
        # 인사 메세지 출력메시지
        print("안녕하세요! 저는 {} 입니다!".format(some_user.name))

    def login(some_user, my_email, my_password):
# 로그인 메소드


user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = "captain@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78945"

print(user1.email)
print(user2.password)
user1.say_hello()
User.say_hello(user2)
