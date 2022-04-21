import pickle
import random
import os ,turtle
def a():
    for i in range(1000):
        fp  = open('D://sda/{0}.txt'.format(str(i)),'w')
        fp.write('sad')
        fp.close()
#a()    
def b():
    fp = open('D://empt.dat','wb')
    for i in range(2):
        n = input('enter : ')
        m = input('enter : ')
        pickle.dump('{0}___{1}'.format(n,m),fp)
    fp.close()
    fp = open('D://empt.dat','rb')
    fp = pickle.load(fp)
    print(fp)

def c():
    with open('D://empty.dat','wb') as fp:
        pickle.dump('computer is a electronic device ',fp)
        fp = open('D://empty.dat','rb') 
        a = pickle.load(fp)
        print(a)    
    #with open('D://empty.dat','rb') as fp:
     #   a = pickle.load(fp)
      #  print(a)
def d():
    fp = open('D:\\empty.dat','rb')
    a = 'computer'
    r = pickle.load(fp)
    print(r)
    if a in r :
        print(True)
    else:
        print(False)
def e():
    for i in range(1000):
        os.remove('D://sda/{}.txt'.format(i))
def f():
    
