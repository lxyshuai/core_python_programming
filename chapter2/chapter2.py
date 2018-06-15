print 'Hello World'
print '%s is number %d!' % ("python", 1)


import sys
print >> sys.stdout, 'Fatal error : invalid input!'
logfile = open('./mylog.txt', 'a')
print >> logfile, 'Fatal error : invalid input!'
logfile.close()


user = raw_input('Enter login name: ')
print 'Your login is:', user
num = raw_input('Now enter a number: ')
print 'Doubling your number: %d ' % (int(num) * 2)


# one comment
def foo():
    '''This is a doc string'''
    return True


print -2 * 4 + 3 ** 2


print 2 < 4
print 2 == 4
print 2 > 4
print 6.2 <= 6
print 6.2 <= 6.2
print 6.2 <= 6.20001


2 < 4 and 2 == 4
2 > 4 or 2 < 4
not 6.2 <= 6
3 < 4 < 5


counter = 0
n = n * 10
n*= 10