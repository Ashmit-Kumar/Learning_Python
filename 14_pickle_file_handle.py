
import pickle
d='abcd'
f=open('abc.txt','wb')
a=pickle.dump(d,f)
f.close()


import pickle
f=open('abc.txt','rb')
a=pickle.load(f)
print(a)
f.close()

