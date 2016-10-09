import sys
import random

hardmax=100

def _get2():
    return(random.randint(1, hardmax - 1), random.randint(1, hardmax - 1))

def print_add_carry(count=1, minum=1, maxnum=hardmax):
    if minnum * 2 >= hardmax:
        raise Exception('min number %s is too large. hardmax is %s' % (minnum, hardmax))
    while count > 0:
        a,b = _get2()
        if a < minum or b < minum or a > maxnum or b > maxnum:
            continue
        if a + b > hardmax or a % 10 + b % 10  < 10:
            continue
        print("%2d + %2d =" % (a,b))
        count -= 1

def print_sub_abdication(count=1, minum=1, maxnum=hardmax):
    while count > 0:
        a,b = _get2()
        if b < minum or a > maxnum:
            continue
        if a - b <= 0 or a % 10 - b % 10  >= 0:
            continue
        print("%2d - %2d =" % (a,b))
        count -= 1

if __name__ == '__main__':
    total = 3
    pattern = 'mix' # add sub mix 
    minnum = 1
    maxnum = hardmax

    argn = len(sys.argv)
    if argn > 1:
        total = int(sys.argv[1])
    if argn > 2:
        pattern = sys.argv[2]
    if argn > 3:
        minnum = int(sys.argv[3])
    if argn > 4:
        maxnum = int(sys.argv[4])

    if pattern == 'mix':
        add = total / 2
        sub = total - add
    elif pattern == 'add':
        add = total
        sub = 0
    else:
        add = 0
        sub = total
    print_add_carry(add, minnum, maxnum)
    print_sub_abdication(sub, minnum, maxnum)

