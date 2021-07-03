##########################################################################

# string = 'sdaaasaaa'
# d={}
# 
# for i in string:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
#         
# print(d)

#########################################################################

from collections import Counter

def find_duplicates(s):
    elements = Counter(s)
    return [k for k,v in elements.items() if v>1]

print(find_duplicates("Hello"))
print(find_duplicates("Hippopotamus"))

#########################################################################

# from collections import Counter
# 
# def alldups(string):
#     cdict = Counter(string)
#     for k, v in cdict.items():
#         if v > 1:
#             print(k)
# 
# #if _name_ == '__main__':
# string = 'geeksforgeeks'
# alldups(string)
