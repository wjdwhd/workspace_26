# 숫자 계산

'''
- 파이썬에서는 숫자의 자료형 (종류)에 따라서 계산 결과가 달라질 수 있음
- 파이썬에서는 숫자를 **정수(int), 실수(float)**, 복소수(complex)로 구분
- 보통 프로그래밍에서는 정수와 실수를 주로 사용
'''

## 정수계산

### 사칙연사

# 덧셈 ( + )
# + : 덧셈 연산자
print(1 + 1) # 2
print(1 + 2) # 3
print(1 + 2 + 3) # 6

# 뺄셈 ( - )
print( 5 - 1 ) # 4
print( 3 - 10 ) # -7

# 곱셈 ( * )
print( 2 * 3 ) # 6
print( 2 * 4 * 5 ) # 40

# 나누셈 ( / )
print( 4 / 2 ) # 2.0
print( 5 / 2 ) # 2.5 -> 소수점이 붙은 수로 '변환'

# 데이터 타입을 확인 할 수 있는 함수
print(type(2 * 2)) # <class 'int'>
print(type(2 / 2)) # <class 'float'>

'''
파이썬에서는 정수끼리 나눗셈 계산을 하더라도, 실수 값을 반환
몫 : 나머지 없이, 나눗셈을 했을 때 정수로 딱 떨어지는 값
몫 연산자 ( // ) - C 계열 언어에서의 주석 표시

- 정수끼리 나눗셈 결과가 실수가 아니라 정수로 나어게 해야할 때 (나머지를 배제해야할 때
- //로 나눗셈을 하시면 됨
- //는 버림 나눗셈 (float division)
'''
print(5 // 2,",", (type(5 // 2))) # 2, <class 'int'>

'''
- 참고로 실수에 // 연산자를 사용하면 결과는 실수가 나오지만 소수점 이하는 버림
- 따라서 (연산자 앞 뒤 숫자 중에 하나라도 실수라면) 결과는 항상 .0으로 끝남
'''
print(5.5 // 2,",", 4 // 2.0 ,",", 4.1 // 2.1) # 2.0 , 2.0 , 1.0

'''
나머지 연산자 ( % )
모듈로 (modulo) 연산자 (모듈러스 ?)
'''
print( 5 % 2 ) # 1

'''
거듭제곱 연산자 ( ** )
루트 사용 - 거듭제곱 연산자에 소수점을 사용
'''
print(2 ** 10 ,",", 2 ** 0.5) # 1024 , 1.4142135623730951

'''
값을 정수로 만들기 ( 소수점 없애기 )
* 계산 결과가 실수 (소수점 있아)로 나왔을 경우에, 강제로 정수로 만들어야할 때는,
* int에 괄호를 붙이고, 숫자 또는 계산식을 넣으면 됨.
* 특히 int(...)에 문자열을 넣어도 정수로 만들 수 있음. 단, 정수로 된 문자열
int (숫자)
int (계산식) ex) int(5/2)
int (문자열) ex) int("1.1"), int("5")
5 ‡ "5"
'''

print(3.3, type(3.3), int(3.3), type(int(3.3)))
print(int(137 / 29)) # /에 int(...) = // 몫 연산자와 같은 작용
print("5", type("5"), int("5"), type(int("5")), 5, type(5))
# int -> 정수 (integer)를 뜻하며, 값을 정수로 만들어줌 (소수점 이하를 버림)

# 몫과 나머지 함계 구하기
print(5 / 2) # 5 / 2 -> 나머지까지 잘개 나눠서 실수화 시켜버림
print(5 // 2, 5 % 2)
print(divmod(5 , 2)) # 5를 2로 나눴을 때의 몫과 나머지를 반환해주는 내장 함수

# 실수 계산
## 실수끼리의 계산 (실수라고 해서 별도의 연산자를 쓰진 않아요)
## 계산하는 대상(피연산자) 중에 하나라도 실수가 들어간다면 무조건 실수처리 (. 붙는다)

## 실수끼리의 덧셈
print(3.5 + 2.1) # 둘 중의 하나가 실수라면
print(3 + 2.1)
print(3.5 + 2)
# 코딩을 배울 때 값을 예측하는 습관 -> 처음에는 내가 예측하는 값이 틀림
# -> (익숙해지면) 내가 코딩한 내용이 틀려서 -> 결과값이 다르게 나옴 (디버깅)

## 실수끼리의 뺄셈
print(4.3 - 2.7) # 부동소수점
print(2.7 - 1.5)
# 컴퓨터는 0,1로 모든 값을 기억한다 -> 2의 배수의 값만 표시 가능
# 10 -> 1010 / 소수점으로 내려가게 되면 -> 더 복잡한 형태로 표시
# 소수점 미만의 작은 오차가 생김 -> 부동소수점

## 실수끼리의 곱셈
print(1.5 * 3.1)

## 실수끼리의 나눗셈
print(5.5 / 3.1)

## 실수화 정수 간의 계산
# - 실수와 정수를 함계 계산하며느 표현 범위가 넓은 실수로 계산됨 (.)
print(4.2 + 5 + 2) # 순서는 상관 없음. 1개 이상이 실수면 실수임.

# 값을 실수로 만들기 ( float )
'''
- float에 괄호를 붙이고 숫자 또는 계산식을 넣으면 변환 (float(...))
- 특히 float에 '믄지열'을 넣어도 실수로 만들 수 있음
- 단, 실수 또는 정수로 된 문자열
float (숫자), float (계산식), float('문자열')
'''

print(
    float(5), float(1+2), float('5.3'), float('5')
)

'''
* float는 부동소수점 (floating point)에서 따왔으며 값을 실수로 만들어줌
* 즉, 실수는 float 자료형
'''

print(type(3.5))

# 괄호 사용 - 계산의 우선 순위, 함수의 실행
print(35 + 1 * 2) # 37 -> * 가 우선순위를 갖는다
# 만약 곱셈보다 덧셈을 먼저 계산하고 싶다면? 덧셈부분을 괄호로 묶어주면 됨
# 어떤 연산자든 괄호에 있는 연산자가 우선 연산됨
print((35 + 1) *  2) # 72