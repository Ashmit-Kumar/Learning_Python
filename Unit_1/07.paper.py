try:
    num=['zero','one','two','three','four']
    s=''
    f=open('ab.txt','r')
    v=f.read()
    f1=open('ab.txt','w')
    for i in v:
        # print(i)
        if i in '0123456789':
            print(i)
            s+=num[int(i)]
        else:
            s+=i
    f1.write(s)
        
    # print(v)
except FileNotFoundError:
    print("File does not exist")
finally:
    f.close()
    f1.close()