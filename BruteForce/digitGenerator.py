n = int(input())
real_n = n
lista = []
for x in range(n):    
    sum_of = 0
    product = 0
    tmp = []
    tmp_n = str(real_n - 1)
    # print(tmp_n)
    for i in range(len(str(tmp_n))):
        tmp.append(str(tmp_n[i]))
    for j in range(len(tmp)):
        sum_of += int(tmp[j])
    product = int(tmp_n) + sum_of
    real_n -= 1
    # print(product)
    if product == n:
        lista.append(tmp_n)
    
print(lista[-1])
