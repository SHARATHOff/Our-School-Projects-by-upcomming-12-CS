#fp =open("d:\\ex1.txt")
#res =fp.read()
#res =fp.read(5)
#print(res)
#res=fp.read(10)
#print(res)
#res =fp.readline()
#print(res)
#res=fp.readline()
#print(res)
#res=fp.readline(2)
#print(res)
#res=fp.readlines()
#print(res)
#for i in res:
 #   print(i)
#res=fp.read()
#for i in res:
 #   a =i.strip()
  #  print(a,end=' ')
#print(res)
#print("Length of the file : ",len(res))
#str1=' '
#while str1:
 #   str1 = fp.readline()
  #  print(str1.rstrip())
#str1=' '
#for i in fp.readlines():
 #   print(i)
#res=fp.readlines()
#print(res)
#for i in res:
 #   print(i)
#fp.close()
######################################
fp =open("d:\\ex2.txt","w")
#fp=open("d:\\ex2.txt","a")
#str1='welcome to computer lab'+'\n'
#fp.write('\n')
#fp.write(str1)
l1=["['welcome home child rose ice'],['welcome home  child  rose ice'],['welcome  home  child  rose ice']","computer lab"]
fp.writelines(l1)
fp.writelines('\n')
fp.writelines(l1)
fp.flush()
fp.writelines("\n")
fp.writelines("hai")
fp.flush()
fp.close()
#fp.close()
