import pickle 
fp = open("d:\q.dat","wb")
pickle.dump("welcome to computer lab",fp)
pickle.dump("computer science",fp)
print("data file created")
fp.close()

