import sys
import random

hardmax=100

def _get2():
    return(random.randint(1, hardmax - 1), random.randint(1, hardmax - 1))

def get_add_carry(count=1, minum=1, maxnum=hardmax):
    ret = [] 
    if minnum * 2 >= hardmax:
        raise Exception('min number %s is too large. hardmax is %s' % (minnum, hardmax))
    while count > 0:
        a,b = _get2()
        if a < minum or b < minum or a > maxnum or b > maxnum:
            continue
        if a + b > hardmax or a % 10 + b % 10  < 10:
            continue
        ret.append("%2d + %2d =" % (a,b))
        count -= 1
    return ret

def get_sub_abdication(count=1, minum=1, maxnum=hardmax):
    ret = []
    while count > 0:
        a,b = _get2()
        if b < minum or a > maxnum:
            continue
        if a - b <= 0 or a % 10 - b % 10  >= 0:
            continue
        ret.append("%2d - %2d =" % (a,b))
        count -= 1
    return ret

if __name__ == '__main__':
    total = 3
    pattern = 'mix' # add sub mix 
    minnum = 1
    maxnum = hardmax

    argn = len(sys.argv)
    if argn > 1:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print('%s total add|sub|mix min max'%(sys.argv[0]))
            sys.exit(0)
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
    li1 = get_add_carry(add, minnum, maxnum)
    li2 = get_sub_abdication(sub, minnum, maxnum)
    li = li1 + li2
    for _ in range(3):
        random.shuffle(li)
    for x in li:
        print('%s'%x)

