# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from string import ascii_uppercase
def solution(N, S, T):
    letter_list = []
    splited_s = []
    S_list = []
    new_axis_list = []

    for i, alphabet_ in enumerate(ascii_uppercase):
        letter_list.append(alphabet_)
    
    Nd_array = [[0] * N] * N

    splited_s = S.split(",")
    print(Nd_array)
    for i in range(len(splited_s)):
        S_list.append(splited_s[i].split())
    for i in range(len(S_list)):
        for j in range(len(S_list)):
            alphabets = (S_list[i][j])[1]
            latter = letter_list.index(alphabets)+1
            new_axis = str((S_list[i][j])[0]) + str(latter)
            new_axis_list.append(new_axis)
    Nd_array[int(new_axis[0])-1][int(new_axis[1])-1] = 1

    print(Nd_array)
    # for i in new_axis_list:
    #     print(int(i[0])-1)
    #     print(int(i[1])-1)
        # print(Nd_array)
solution(4,"1A 1B,2C 2C","1B")