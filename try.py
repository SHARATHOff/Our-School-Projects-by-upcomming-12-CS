fp = open('D:\\ewq.txt','r')
#for i in range(100):
 #   fp.write(str(i))
  #  fp.write('\n')
#fp.close()
#fp = open('D:\ww.txt','r')
a = fp.readlines()

for i in a:
    print(i.strip())


    
