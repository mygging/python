#로또번호를 랜덤으로 뽑아주는 프로그램을 짜자

import random

numbers = range(1,46)
#마치 [1,2,3,....45]와 비슷하다. 마지막 숫자는 포함하지 않는다.
#6개의 숫자를 뽑아 출력해 주는 프로그램 작성

#알트 + 쉬프트 + 위 아래 방향키 = 복사됨
#알트만 누르고 방향키하면 줄이 이동함
print(random.choice(numbers))
#숫자가 중복되는 문제가 발생함

lotto = random.sample(numbers,6)

print(lotto)

print(sorted(lotto))  #sorted는 정렬이다 세로에서 가로로

