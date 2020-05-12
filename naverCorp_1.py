# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    count = 0
    count_list = []
    for i in range(len(A)):
        count = 0
        for j in range(0, len(A)):
            if i != j:
                if A[i] == 1 and A[j] == 6:
                    count += 2
                elif A[i] == 2 and A[j] == 5:
                    count += 2
                elif A[i] == 3 and A[j] == 4:
                    count += 2
                elif A[i] == 4 and A[j] == 3:
                    count += 2
                elif A[i] == 5 and A[j] == 2:
                    count += 2
                elif A[i] == 6 and A[j] == 1:
                    count += 2
                elif A[i] == A[j] and A[j] == A[i]:
                    count += 0
                elif A[i] != A[j] and A[j] != A[i]:  
                    count += 1
            else:
                pass
        count_list.append(count)
    return min(count_list)



