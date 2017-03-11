#!/usr/bin/env python

import os, sys

def rotor(test_array, k):
    ret = []
    ilen = len(test_array)
    n,m=0,0
    if k <= ilen:
       n = ilen // k
       m = ilen % k


    for i in range(n):
        spos = i*k
        epos = (i+1)*k
        ta = test_array[spos:epos]
        ta.reverse()
        ret.extend(ta)

    if m != 0:
        ret.extend(test_array[n*k:])
    return ret

def compare(act, exp):

    if len(act) != len(exp):
        return False

    for i in range(len(act)):
        if act[i] != exp[i]:
            return False

    return True

def main():

    test_array = [1, 2, 3, 4, 5, 6, 7, 8]

    k = 1
    expect_arry = [1, 2, 3, 4, 5, 6, 7, 8]
    ret = rotor(test_array, k)
    print('k = %d, results %s' %(k, compare(ret, expect_arry)))

    k = 2
    expect_arry = [2, 1, 4, 3, 6, 5, 8, 7]
    ret = rotor(test_array, k)
    print('k = %d, results %s' % (k, compare(ret, expect_arry)))

    k = 3
    expect_arry = [3, 2, 1, 6, 5, 4, 7, 8]
    ret = rotor(test_array, k)
    print('k = %d, results %s' % (k, compare(ret, expect_arry)))

    k = 4
    expect_arry = [4, 3, 2, 1, 8, 7, 6, 5]
    ret = rotor(test_array, k)
    print('k = %d, results %s' % (k, compare(ret, expect_arry)))

    # 如果k的值比数组本身长度大，则重置k值为数组长度
    k = 9
    expect_arry = [8, 7, 6, 5, 4, 3, 2, 1]
    ret = rotor(test_array, k)
    print('k = %d, results %s' % (k, compare(ret, expect_arry)))



if __name__ == '__main__':
    sys.exit(main())





