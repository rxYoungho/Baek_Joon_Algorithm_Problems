n, m = map(int,input().split())
# print(n,m)
num_list = list(input().split())
# print(num_list)

sum_list = []
for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        for e in range(j+1, len(num_list)):
            sum_list.append(int(num_list[i])+int(num_list[j])+int(num_list[e]))
sum_list.sort()
for x in range(len(sum_list)):
    if sum_list[x] == m:
        print(sum_list[x])
        break
    elif sum_list[x] > m:
        print(sum_list[x-1])
        break
    elif sum_list[-1] < m:
        print(sum_list[-1])
        break
# print(sum_list)