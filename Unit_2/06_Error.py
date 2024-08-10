# def rprint(lst):
#     # Base case: If the list is empty, do nothing
#     if not lst:
#         return
    
#     # Recursive case: Print the last element and call rprint on the rest of the list
#     print(lst[-1])
#     rprint(lst[:-1])  # Recursive call with all elements except the last one

# # Example usage:
# rprint([1, 2, 3])  # Output: 3 2 1
# rprint([])


def removekth(s,k):
    if len(s)<k:
        return s
    c=0
    s1=''
    while c!=k:
        s1+=s[c]
        c+=1
    else:
        s1+=s[k+1:len(s)]
    return s1

print(removekth("Python",1))
print(removekth("Python",3))
print(removekth("Python",0))
print(removekth("Python",20))