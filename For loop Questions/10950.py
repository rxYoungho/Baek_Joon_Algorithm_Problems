# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

#입력    출력
# 1 1     2
# 2 3     5
# 3 4     7
# 9 8     17
# 5 2     7

testcase = int(input())
listA = []
for i in range(testcase):
    a, b = map(int,input().split())
    listA.append(a+b)
    
for x in listA:
    print(x)