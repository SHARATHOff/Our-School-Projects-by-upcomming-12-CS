#import sys

#res1=input("Enter the text : ")
#res2=input("Enter the text 2 : ")

#sys.stdout.write(res1)#
#sys.stdout.write('\n'+'\t')
#sys.stdout.write(res2)

import pickle

#fp = open("d:\stu.dat","ab+")
#pickle.dump("vidyaa vikas",fp)
#pickle.dump("varahoorampatti",fp)
#fp.close()
#fp =open("d:\stu.dat","rb")
#res1={}
#try:
 #   while True:
  #      res1=pickle.load(fp)
  #      print(res1)
#except EOFError:
 #   fp.close()

stu ={}
stufile = open("d:\\stu1.dat","wb")
ans1='y'
while ans1=='y':
    rno = int(input("enter the rollno. :"))
    name =input("Enter te name :")
    marks=float(input("Enter the marks : "))
    stu['rollno']=rno
    stu['name']=name
    stu['marks']=marks
    pickle.dump(stu,stufile)
    ans1=input("Do you want to continue (y/n)..")

stufile.close()
            
  
stu ={}
found =False
stufile = open("d:\\stu1.dat","rb")
searchkeys=[12,14]
try:
    print("searching in files stu,dat...")
    while True:
        stu=pickle.load(stufile)
        if stu['rollno'] in searchkeys:
            print(stu)
            found = True
except EOFError:
    if found == False:
        print("no such records")
    else:
        print("search successful")
stufile.close()





        




        


    














