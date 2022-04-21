#def fun(a):
  #  print('\t inside my fun()')
   # print('\t value recived in a as ',a)
    #a=a+2
    #print('\t value of"a"now change to',a)

#n=int(input('enter a number;'))
#fun(n)

def fun(n):
    import math
    m=math.cos(n)
    print(m)
    return m

x=int(input('enter no:'))
fun(x)
