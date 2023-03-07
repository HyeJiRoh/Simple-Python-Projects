import random

num = random.randint(1, 100)
count = 1

print("==================GAME START==================")

while True:
    try:
        print()
        my_number = int(input("1~100까지의 숫자를 입력하세요 : "))

        if my_number > num:
            print("입력하신 숫자보다 작습니다.")
        elif my_number < num:
            print("입력하신 숫자보다 큽니다.")
        else:
            print()
            print("⭐️정답입니다!⭐️")
            print("당신은 %d번만에 맞추셨습니다."%count)
            print()
            print("===================GAME END===================")
            break

        count += 1

    except:
        print("에러가 발생했습니다. 정수만 입력 가능합니다.")