#!/usr/bin/python
#encoding:utf-8
import sys

b = u'汉字123'

print 'unicode', b, 'len',len(b)

li=[s for s in b]
findit = False
for x in li:
    if x.isalnum() == True:
        if  x.isdigit() == True:
            findit = True
        break
if findit == True:
   print('除去汉字之后，字符串以数字开头')
else:
   print('除去汉字之后，字符串不以数字开头')
print('以上测试有误。')

b = u'汉字_123'
c = b.encode('utf-8')
print 'utf-8', c, 'len', len(c)
print('utf-8 :')
li=[s for s in c]
findit = False
for x in li:
    print ord(x)
    if ord(x) < 128:
        print(x)
        if  x.isdigit() == True:
            findit = True
        break
if findit == True:
   print('除去汉字之后，字符串以数字开头')
else:
   print('除去汉字之后，字符串不以数字开头')
print('以上测试正确。')
print('结论：使用utf-8编码的str来进行判断是可行方法。')

def ishostname(utf8str):
    c = utf8str
    li=[s for s in c]

    if li[0].isalpha() == False:
       return False

    ret = True
    for x in li[1:]:
        if x.isalnum() == True or x == '-':
            continue
        ret = False
        break
    if li[-1] == '-':
        ret = False
    return ret

if __name__=='__main__':
    print("请使用UTF-8格式字符串")
    b = 'a1-23-'
    if len(sys.argv) == 2:
        b = sys.argv[1]
    if ishostname(b):
        print('%s 是合法主机名。' % b)
    else:
        print('%s 不是合法主机名。' % b)
