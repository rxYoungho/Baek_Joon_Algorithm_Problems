#자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
import sys

n = int(sys.stdin.readline())
listA = []

for i in range(n+1):
    if i > 0:
        listA.append(i)

for x in range(n+1):
    if x > 0:
        print(listA[-x])