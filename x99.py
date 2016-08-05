from __future__ import print_function

def print9x9(mod=0, space=3, start=1, end=9):
    to = end + 1
    for i in range(start, to):
        if mod == 0:
            to = i + 1
        for j in range(start, to):
            x = min(i,j)
            y = max(i,j)
            print('%i x %i = %2i' % (x, y, x*y) + ' ' * space, end="")
        print('')
    print('')

if __name__=='__main__':
        print9x9()
        print9x9(1)
        print9x9(space=2, start=11, end=19)

