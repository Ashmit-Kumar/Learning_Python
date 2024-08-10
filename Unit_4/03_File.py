# Writing in a file
'''
to write you have
1)write()
2)writelines()
'''

f=open('aa.txt','w')
f.write("Hello how are you \nToday is a beautiful day\nWe love this weather ")
f.close()


#using  with 

with open('bb.txt','w') as file:
    file.writelines(['hello how are','you','this is a beautiful planet\n','we would love to line in this planet'])
    

# Append 
file=open('abc.txt','a')
file.write('\nThis is appended file')
file.close()