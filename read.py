fp=open("text.txt","w")
str=input("enter the name:")
fp.write (str1)
fp=close()
fp1=open("text.txt","r")
str2=fp1.read()
print(str2)
fp1.close()
         

def fact(s):
    fs=1
    for p in range(1,s+1):
        fs*=p
        print("factorial of",p, "is,fs" ) 
        h=int(input("to find factorial of:"))
        fact(h)
