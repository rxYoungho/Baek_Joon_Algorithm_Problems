n = int(input())

#from n - 1, keep going down and compare
tmp = n-1

# for i in range(len(str(tmp))):
#     guess = tmp+tmp[0]

guess = tmp + tmp[0] + tmp[1]

print(guess)