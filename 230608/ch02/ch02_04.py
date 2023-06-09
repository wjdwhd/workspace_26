# 출력

## 값을 여러 개 출력하기
'''
print에는 변수나 값 여러 개를, (콤마)로 구분하여 넣을 수 있음
print (값1, 값2, 값3)
print (변수1, 변수2, 변수3)
'''

print(1, 2, 3) # 1 2 3
print('뱀', '고양이') # 뱀 고양이
a = 10 # 10
print(10, a, "10") # 10 10 10
# 여러 개의 값을 넣을 때, 기본적으로 print (츨력) 시에 ''로 구분해줌
print(1, 2, 3, 4, 5, 6, 7, 8, 9) # 1 2 3 4 5 6 7 8 9
print(1,2,3,4,5,6,7,8,9) # 1 2 3 4 5 6 7 8 9
# print에 변수나 값을 콤마로 구분해서 넣으면 각 값이 공백으로 띄워져서 한 줄로 출력
# (값을 여러 개 출력할 때 print 함수를 여러 번 쓰지 않아도 됨)

# 구분자를 변환
'''
값 사이에 공백이 아닌 다른 문자를 넣고 싶을 때는
print의 sep에 문자 또는 문자열을 지정(sep는 구분자라는 뜻의 separator에서 따옴)
print (값1, 값2, sep='문자 또는 문자열')
print (변수1, 변수2, sep='문자 또는 문자열')
'''
print(1, 2, 3, sep=',') # 1,2,3
print(1, 2, 3) # 1 2 3
print('그냥', '공백없이', '붙어있었으면', sep='') # 그냥공백없이붙어있었으면
print('그냥', '공백없이', '붙어있었으면', sep=' ') # 그냥 공백없이 붙어있었으면
# 이게 기본 sep

# 줄 바꿈 활용하기
# print에 값을 여러 개 지정하면 한 줄에 모든 값이 츨력
print("개", "고양이", "돼지")
# sep => 개행 문자 (줄바꿈 문자 = Enter = \n)라는 특별한 문자를 지정하면...
print(1, 2, 3, sep="\n") # 값을 한 줄에 하나씩 출력함
'''
1
2
3
'''
print("1\n2\n3") # 비슷한 결과 (\n은 문자열에 섞이면 줄바꿈 역할을 함)
'''
1
2
3
'''

# end 사용하기
# print ("...", sep = "", end="\n")
'''
print (값, end = '문자 또는 문자열')
print (변수, end = '문자  또는 문자열')
'''

print(1) # 1
print(2) # 2
print(3) # 3

print(1, end='') # \n -> ''
print(2, end='') # \n -> ''
print(3, end='') # \n -> ''
# 123
print("")
print(1, end=' ') # \n -> ' '
print(2, end=' ') # \n -> ' '
print(3, end=' ') # \n -> ' '
# 1 2 3
#----------------------------------------
# 한국은 숫자를 만의 단위로 끊어서 표현
# 미국은 숫자를 천의 단위로 끊어서 표현 -> 미국에서 파이썬이 만들어짐
print("")
print(1000000) # 1000000
print(1_000_000) # 1000000
# 천의 단위씩 _로 나눠서 푷현할 수 있음
# 3자리마다 _(밑줄 문자)를 사용해서 큰 숫자 나눠서 표현 가능

