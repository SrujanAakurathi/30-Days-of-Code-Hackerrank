ret_d, ret_m, ret_y = [int(x) for x in input().split(' ')]
exp_d, exp_m, exp_y = [int(x) for x in input().split(' ')]
if (ret_y, ret_m, ret_d) <= (exp_y, exp_m, exp_d):
    print(0)
elif (ret_y, ret_m) == (exp_y, exp_m):
    print(15 * (ret_d - exp_d))
elif ret_y == exp_y:
    print(500 * (ret_m - exp_m))
else:
    print(10000)