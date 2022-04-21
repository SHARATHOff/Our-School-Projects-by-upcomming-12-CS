import pickle
stu ={}
stufile = open("d:\\stu1.dat","wb")
ans1='y'
while ans1=='y':
    rno = int(input("enter the rollno. :"))
    name =input("Enter te name :")
    marks=int(input("Enter the marks : "))
    stu['rollno']=rno
    stu['name']=name
    stu['marks']=marks
    pickle.dump(stu,stufile)
    ans1=input("Do you want to continue (y/n)..")

stufile.close()
            
  
#stu ={}
#found =False
#stufile = open("d:\\stu1.dat","rb")
#searchkeys=[12,14]
#try:
 #   print("searching in files stu,dat...")
  #  while True:
   #     stu=pickle.load(stufile)
    #    if stu['rollno'] in searchkeys:
     #       print(stu)
      #      found = True
#except EOFError:
 #   if found == False:
  #      print("no such records")
   # else:
    #    print("search successful")
#stufile.close()


stu={}
found=False
fin = open("d:\stu.dat","rb+")
try:
    while True:
        rpos = fin.tell()
        stu= pickle.load(fin)
        if int(stu[2])>81:
            stu[2]+=2
            fin.seek(rpos)
            pickle.dump(stu,fin)
            found=True
except EOFError:
    if found==False:
        print("sorry , no matching record found")
    else:
        print("Record(s) successfully updated")
fin.close()

