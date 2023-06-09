#불(bool), 비교, 논리 연산자

# 불(bool)과 비교, 논리 연산자
## 불(bool)과 비교 연산자 사용하기

'''
* 프로그래밍 -> 참(true), 거짓(false) 판단 -> 참(true) : 어떠한 조건이나 수식을 만족시키는가 ? / 거짓 (false) : 만적시키지 못한다
* 불 (bool) 혹은 불리인 (boolean) : 참과 거짓으로 구성된 자료형 <- 조건이나 수식들이 존재하게 됨
# 두 값의 관계를 판단하는 비교 연산자 / 드 값의 논리적 관계를 판단하는 논리 연산자
# if, while.. 구문을 작성
'''

print(True, False) # True False
# 다른 언어들은 대개 true false
print(int(True), int(False)) # 1, 0

# 비교 연산자 - 판단 결과
## 등호(같다, 다르다) 와 부등호(크다, 작다) -> 비교하는 식이 맞으면 True 아니면 False
print('10 > 5', '10이 5보다 크다, 10은 5를 초과한다', 10 > 5) # 10 > 5 10이 5보다 크다, 10은 5를 초과한다 True
print('10 < 5', '10이 5보다 작다, 10은 5를 미만한다', 10 < 5) # 10 < 5 10이 5보다 작다, 10은 5를 미만한다 False

## 숫자가 같은지 다른지 비교
'''
* 일반적 수학에서는 =(등호)로 쓰는데, 파이썬등 프로그래밍에서는 ==을 등호(동등 연산자, equal)로 쓴다
* =(등호)는 파이썬에서 뭘까요 ? -> 대입 연산자 -> 특정한 변수에 값을 할당해주는 연산자
* 다를 때 != (not equal)을 사용
'''
print("1 == 1", 1 == 1)
print("2 == 1", 2 == 1)
print("1 == 1", 1 != 1)

## 문자열 등등 여부 비교
print("'python' == 'python'", 'python' == 'python') # 'python' == 'python' True
# java : == (x), equals -> 주소 값을 비교하기 때문
print("'python' == 'Python'", 'python' == 'Python') # 'python' == 'Python' False
print("'Python' == 'python'", 'Python' == 'python') # 'Python' == 'python' False
# 대소문자가 다르면 다른 문자로 판별

# 숫자 비교 : 부등호
print("10 > 20", 10 > 20) # 10 > 20 False -> 초과
print("10 < 20", 10 < 20) # 10 < 20 True -> 미만
print("10 >= 20", 10 >= 20) # 10 >= 20 False -> 이상
print("10 <= 20", 10 <= 20) # 10 <= 20 True  -> 이하

# 객체가 같은지 다른 지 비교하기
'''
* is, is not -> 연산자. ==, !=. 왜 is (~ 이다), is not (~가 아니다)?
* ==, != : 값 자체를 비교한다
* is, is not -> 객쳊를 비교한다, 객체를 비교한다 (타입)
'''
print("1 == 1.0 : ", 1 == 1.0) # 1 == 1.0 :  True
# 1이라고 하는 '깂'은 같아요 ( 상호 변환이 가능 ) - 같은 숫자형일 경우에는 같다고 함
print("'1' == 1 : ", '1' == 1.0) # '1' == 1 :  False
# 문장열과 숫자의 비교이므로 성립 안함
# javascript 에선 위와 같은 코드를 성립한다.
a = 1 is 1.0 # 비교 연산의 결과 값을 변수에 담을 수 있음
print("1 is 1.0 : ", a) # 1 is 1.0 : False
b = (1 is not 1.0)
print("1 is not 1.0 : ", b) # 1 is not 1.0 : true

# 논리 연산자 사용하기
## 논리연산자는 and, or, not (연산자가 꼭 특수문자나 기호일 필요는 없음)
'''
(java, C - 기호)

and - & &&
or - | ||
not - !
'''

## and(그리고) 연산자
have_car = True
have_money = True
can_drive = have_car and have_money # 하나라도 false면은 전부 false
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
'''
have_car True
have_money True
can_drive True
'''
have_car = False
have_money = True
can_drive = have_car and have_money # 하나라도 false면은 전부 false
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
'''
have_car False
have_money True
can_drive False
'''
have_car = True
have_money = False
can_drive = have_car and have_money # 하나라도 false면은 전부 false
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
'''
have_car True
have_money False
can_drive False
'''
have_car = False
have_money = False
can_drive = have_car and have_money # 하나라도 false면은 전부 false
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
'''
have_car False
have_money False
can_drive False
'''

print("have_car & have_money", have_car & have_money) # have_car & have_money False
# print("have_car && have_money", have_car && have_money)
# java에서 가능한 문법 &&
# 문법 오류

# or / a or b : or 로 ( a | b )
hungry = True
study = True
have_lunch = hungry or study
print("hungry", hungry) # hungry True
print("study", study) # study True
print("have_lunch", have_lunch) # have_lunch True

hungry = False
study = True
have_lunch = hungry or study
print("hungry", hungry) # hungry False
print("study", study) # study True
print("have_lunch", have_lunch) # have_lunch True

hungry = True
study = False
have_lunch = hungry or study
print("hungry", hungry) # hungry True
print("study", study) # study False
print("have_lunch", have_lunch) # have_lunch True

hungry = False
study = False
have_lunch = hungry or study
print("hungry", hungry) # hungry False
print("study", study) # study False
print("have_lunch", have_lunch) # have_lunch False
# or 연산의 단축키 '|'
print("hungry | study", hungry | study) # hungry | study False

# not (논리값 -> bool) True -> False / False -> True
sleepy = True
print("sleepy", sleepy) # sleepy True
print("not sleepy", not sleepy) # not sleepy False
# print("not sleepy", ! sleepy) -> '!' 연산자는 없음

# and, or, not -> not (1), and (2), or (3)

print("not True and False or not False", not True and False or not False) # not True and False or not False True
print("(not True) and False or (not True)", False and False or True) # (not True) and False or (not True) True
print("(not True) and False or (not False)", False or True) # (not True) and False or (not False) True
# 논리 연산도 ()를 통해서 강제로 우선순위를 정해줄 수 있음
# 논리 연산을 복잡하게 하는 것에 익숙하지 않다 / 못하겠다 라는 마음이 있다면 하는 방법
# 1. 괄호 사용 -> 2. 변수로 끊어서 연산하기

# 논리 연산자 + 비교 연산자 (무조건 비교 연산자가 먼저임)
# 비교 연산자를 통해서 값을 비교하고 이것을 통해 True 또는 False 결과값 (bool 값이 나옴)
# 그 후에 논리 연산자가 그것을 받아서 처리함
# 산술 -> 비교 -> 논리 연산자 순서 (그래도 괄호와 변수로 표현된 건 먼저 처리가 된 상태임)
print("10 == 10 and 10 != 5 :", 10 == 10 and 10 != 5) # 10 == 10 and 10 != 5 : True
print("(10 == 10) and (10 != 5) :", (10 == 10) and (10 != 5)) # (10 == 10) and (10 != 5) : True
print("10 > 5 or 10 < 3", 10 > 5 or 10 < 3) # 10 > 5 or 10 < 3 True
print("5 + 5 > 8 and (3 - 2) < 0", 5 + 5 > 8 and 3 - 2 < 0) # 5 + 5 > 8 and (3 - 2) < 0 False
print("(5 + 5) > 8 and (3 - 2) < 0", (5 + 5) > 8 and (3 - 2) < 0) # (5 + 5) > 8 and (3 - 2) < 0 False
print("not 10 > 5", not 10 > 5) # not 10 > 5 False
print("not 7 + 3 > 5", not 7 + 3 > 5) # not 7 + 3 > 5 False

# 정수, 실수, 문자열을 불 (참, 거짓)으로 만들기 / 판별
'''
정수, 실수, 문자열 -> 불(bool) => bool(1)
'''

print("bool(1) : ", bool(1)) # bool(1) :  True
print("bool(-1) : ", bool(-1)) # bool(-1) :  True
# 정수, 실수나 => 숫자에서는 True/False 기준은 0 이면 False / 0 이 아니면 True
print("bool(0) : ", bool(0)) # bool(0) :  False
# number -> bool ???? number != 0

# 문자열
print("bool('아무거나') : ", bool('아무거나')) # bool('아무거나') : True
print("bool('아무거나') : ", bool('아무11거나')) # bool('아무거나') : True
print("bool('') : ", bool('')) # bool('') :  False
# 큰따음표 또는 작은따옴표로 감싸진 것만 있을 때
# string -> bool ???? len(string) > 0
# length (길이)

