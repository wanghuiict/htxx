import sys
import random

maxnum=100

def _get2():
    return(random.randint(1, maxnum - 1), random.randint(1, maxnum - 1))

def print_add_carry(count=1, minum=1):
    if minnum * 2 >= maxnum:
        raise Exception('min number %s is too large. maxnum is %s' % (minnum, maxnum))
    while count > 0:
        a,b = _get2()
        if a < minum or b < minum:
            continue
        if a + b > maxnum or a % 10 + b % 10  < 10:
            continue
        print("%2d + %2d =" % (a,b))
        count -= 1

def print_sub_abdication(count=1, minum=1):
    while count > 0:
        a,b = _get2()
        if a < minum or b < minum:
            continue
        if a - b <= 0 or a % 10 - b % 10  >= 0:
            continue
        print("%2d - %2d =" % (a,b))
        count -= 1

if __name__ == '__main__':
    total = 3
    minnum = 10
    pattern = 'mix' # add sub mix 
    argn = len(sys.argv)
    if argn > 1:
        total = int(sys.argv[1])
    if argn > 2:
        minnum = int(sys.argv[2])
    if pattern == 'mix':
        add = total / 2
        sub = total - add
    elif pattern == 'add':
        add = total
        sub = 0
    else:
        add = 0
        sub = total
    print_add_carry(add, minnum)
    print_sub_abdication(sub, minnum)

