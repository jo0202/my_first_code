a = input("첫번째 숫자 입력하기: ")

b = input("두번째 숫자 입력하기: ")

print("입력한 숫자는 다음과 같습니다: {} {}".format(a, b))

print("입력한 숫자의 자료형은 다음과 같습니다:", type(a), type(b))

print("입력한 숫자의 사칙연산을 실행합니다.")
plus = float(a) + float(b)
minus = float(a) - float(b)
multiplication = float(a) * float(b)
division = float(a) / float(b)

print("a + b =", plus, "|", "a - b =", minus, "|", "a * b =", multiplication, "|", "a / b =", division, "|")

