# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력: 3
# 출력: 6
a = 0
n =  int(input())
for i in range(n+1):
    if i > 0:
        a += i
print(a)
