# you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
# public String solve(int A, int B, int C, int D, int E, int F) {
#   int[] d = {A, B, C, D, E, F};
#   Arrays.sort(d);
#   if (d[4] < 6) { // 2nd largest digit is smaller 6, we can just fill up
#     if (10 * d[0] + d[1] < 24)
#       return "" + d[0] + d[1] + ":" + d[2] + d[3] + ":" + d[4] + d[5];
#     else
#       return "impossible";
#   } else if (d[3] < 6) { // 3rd largest digit is smaller 6, put 2nd largest in 4th position
#     if (10 * d[0] + d[1] < 24)
#       return "" + d[0] + d[1] + ":" + d[2] + d[4] + ":" + d[3] + d[5];
#     else
#       return "impossible";
#   } else if (d[2] < 6) { // 4th largest digit is smaller 6, put 3rd largest in 2nd position
#     if (10 * d[0] + d[3] < 24)
#       return "" + d[0] + d[3] + ":" + d[1] + d[4] + ":" + d[2] + d[5];
#     else
#       return "impossible";
#   } else {
#       return "impossible";
#   }
# }

def solution(A, B, C, D, E, F):
    num_list = []
    
    num_list.append(A)
    num_list.append(B)
    num_list.append(C)
    num_list.append(D)
    num_list.append(E)
    num_list.append(F)

    num_list.sort()
    
    if num_list[4] < 6:
        if int(str(num_list[0]) + str(num_list[1])) < 24:
            return str(num_list[0])+str(num_list[1])+":"+str(num_list[2])+str(num_list[3])+":"+str(num_list[4])+str(num_list[5])
        else:
            return "NOT POSSIBLE"
    elif num_list[3] < 6:
        if int(str(num_list[0]) + str(num_list[1])) < 24:
            return str(num_list[0])+str(num_list[1])+":"+str(num_list[2])+str(num_list[4])+":"+str(num_list[3])+str(num_list[5])
        else:
            return "NOT POSSIBLE"
    elif num_list[2] < 6:
        if int(str(num_list[0]) + str(num_list[3])) < 24:
            return str(num_list[0])+str(num_list[3])+":"+str(num_list[1])+str(num_list[4])+":"+str(num_list[2])+str(num_list[5])
        else:
            return "NOT POSSIBLE"
    else:
        return "NOT POSSIBLE"
    # high.sort()
    # low.sort()
    # high_len = len(high)
    # low_len = len(low)

    # if high_len > low_len:
    #     return "NOT POSSIBLE"
    # if high_len == low_len:
    #     return str(num_list[0])+str(num_list[1])+":"+str(num_list[2])+str(num_list[3])+":"+str(num_list[4])+str(num_list[5])
    # if high_len < low_len:
    #     if high_len == 0 or high_len == 1:
    #         return str(num_list[0])+str(num_list[1])+":"+str(num_list[2])+str(num_list[3])+":"+str(num_list[4])+str(num_list[5])
    #     if high_len == 2:
    #         num_list[3], num_list[4] = num_list[4], num_list[3]
    #         print(num_list)
    #         return str(num_list[0])+str(num_list[1])+":"+str(num_list[2])+str(num_list[3])+":"+str(num_list[4])+str(num_list[5])
           
        
    
    # return HH,":", MM,":", SS


print(solution(0,0,0,7,8,9))