import random

def _get2():
    return(random.randint(1,99), random.randint(1,99))

def print_add_carry(count=1):
    while count > 0:
        a,b = _get2()
        if a + b > 100 or a % 10 + b % 10  < 10:
            continue
        print("%2d + %2d =" % (a,b))
        count -= 1

def print_sub_abdication(count=1):
    while count > 0:
        a,b = _get2()
        if a - b <= 0 or a % 10 - b % 10  >= 0:
            continue
        print("%2d - %2d =" % (a,b))
        count -= 1

if __name__ == '__main__':
    print_add_carry(3)
    print_sub_abdication(3)
