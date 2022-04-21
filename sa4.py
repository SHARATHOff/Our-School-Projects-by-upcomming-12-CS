import csv
#fp =open("d:\\ex1.csv","w")
#fw =csv.writer(fp,delimiter='|')
#fw.writerow(['rollno','sname','marks'])
#fw.writerow([34,'vidyaa',65])
#l1=[[45,'rose',78],[56,'jasmin',90],[56,'nithi',99],[67,'lotus',78]]
#fw.writerows(l1)
#fp.close()
fp=open("d:\\ex2.csv","r")
fr= csv.reader(fp,delimiter='')
    for r1 in fr:
    print(r1)
print(fr)

 with open("d:\\ex2.csv","r") as fh:
    fr1= csv.reader(fh)
    for r1 in fr1:
        print(r1)
