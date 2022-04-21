#import sys
#fh = open("d:\ex1.txt")
#l1=fh.readline()
#l2 =fh.readline()
#sys.stdout.write(l1)
#sys.stdout.write(l2)
#sys.stderr.write("NO errors occured")

#with open("d:\ex1.txt","r") as fp:
 #   res=fp.read()
  #  print(res)
    
#with open("d:\ex3.txt","w") as fp:
 #   fp.write("hai")
  #  fp.write("\n")
   # fp.write("welcome")
    #fp.write("\n")
    #fp.write("home")
import pickle

#fp = open("d:\stu.dat","wb")

pickle.dump("welcome to computer lab",fp)
pickle.dump("computer science",fp)
print("data file created")
fp.close()
  
#fp=open("d:\stu.dat","rb")
#x=' '
#x=pickle.load(fp)
#print(x)
#x=pickle.load(fp)
#print(x)

