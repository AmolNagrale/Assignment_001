import re
# pattern=re.compile('python')
# print(type(pattern))
#
# matcher=pattern.finditer('Learn python is very easy')


# count=0
# pattern=re.compile('bb')
# matcher=pattern.finditer('abaababa')
# for match in matcher:
#     count+=1
#     print('match is available at start index is:',match.start())
# print('The number of occurances:',count)


# import re
# count=0
# pattern=re.compile('ab')
# matcher=pattern.finditer('abaababa')
# for m in matcher:
#     count+=1
#     print('start: {},end: {},group: {}'.format(m.start(),m.end(),m.group()))
# print('The total occurance is:', count)

#=========================================
# without using compile
# import re
# count=0
# matcher=re.finditer('ab','abaababa')
# for m in matcher:
#     count+=1
#     print('start: {},end: {},group: {}'.format(m.start(),m.end(),m.group()))
# print('The total occurance is:', count)

#============================================
# charecter classes
#import re
#matcher=re.finditer('[abc]','a7b@k9z')
#matcher=re.finditer('[^abc]','a7b@k9z')
#matcher=re.finditer('[0-9]','a7b@k9z')
#matcher=re.finditer('[a-zA-Z0-9]','a7b@k9z')
# matcher=re.finditer('[^a-zA-Z0-9]','a7b@k9z')
# for m in matcher:
#     print(m.start(),'...........',m.group())
    
#==============================================

#predefined Charecter classes
#import re
#matcher=re.finditer('\s','a7b @k9z')
#matcher=re.finditer('\S','a7b @k9z')
#matcher=re.finditer('\d','a7b @k9z')
#matcher=re.finditer('\D','a7b @k9z')
#matcher=re.finditer('\w','a7b @k9z')
#matcher=re.finditer('\W','a7b @k9z')
# matcher=re.finditer('.','a7b @k9z')
# for m in matcher:
#     print(m.start(),'...........',m.group())
    
#===============================================
import re
#Quatifiers
# matcher=re.finditer('a','aababaaaaaba')
# matcher=re.finditer('a+','aababaaaaaba')
# matcher=re.finditer('a*','aababaaaaaba')
# matcher=re.finditer('a?','aababaaaaaba')
# matcher=re.finditer('a{3}','aababaaaaaba')
# matcher=re.finditer('a{2,3}','aababaaaaaba')
#matcher=re.finditer('a{2}a*','aababaaaaaba')
#matcher=re.finditer('a{9}a*','aababaaaaaba')
#matcher=re.finditer('[^a]','aababaaaaaba')
#matcher=re.finditer('^a','aababaaaaaba')
# matcher=re.finditer('a$','aababaaaaaba')
# for m in matcher:
#     print(m.start(),'...........',m.group())

#==================================================

# Important fuctions of re module:
#match()
# import re
# s=input('Enter pattern to check:')
# m=re.match(s,'abcdefgh')
# if m!=None:
#     print('Match is available at begining of the string')
#     print('Start Index:{} and End Index:{}'.format(m.start(),m.end()))
# else:
#     print('Match is not available at the begining of the string')
#================================================================

#fullmatch()

# import re
# s=input('Enter pattern to check:')
# m=re.fullmatch(s,'abcdefgh')
# if m!=None:
#     print('Match is available at begining of the string')
#     print('Start Index:{} and End Index:{}'.format(m.start(),m.end()))
# else:
#     print('Match is not available at the begining of the string')
#=============================================================

#search()

# import re
# s=input('Enter pattern to check:')
# m=re.search(s,'abaabaaab')
# if m!=None:
#     print('Match is available')
#     print('First occurance with Start Index:{} and End Index:{}'.format(m.start(),m.end()))
# else:
#     print('Full string not available')
#
#===================================================
# findall():
# import re
# l=re.findall('[0-9]','a7b9k6z')
# print(l)

#========================================================

# #sub()
# import re
# #s=re.sub('\d','#','a7b9k5t9k')
# s=re.sub('\d','**','a7b9k5t9k')
# print(s)

#==================================================

# # #subn():
# import re
# t=re.subn('\d','**','a7b9k5t9k')
# print(type(t))
# print('The result String:',t[0])
# print('The number of replacements:',t[1])

#===================================================

# import re
# #l=re.split('\.','www.durgasoftvideos.com')
# l=re.split(",","'sunny','bunny','chinny','vinny','pinny'")
# #print(l)
# for t in l:
#     print(t)
 
#=====================================================

# #^ symbol
# import re
# s = 'Learning python is very easy'
# res=re.search('^Learn',s)
# if res!=None:
#     print('Target string starts with Learn')
# else:
#     print('Target string not starts with Learn')

#===================================================

# # $ symbol
# import re
# s = 'Learning python is very easy'
# res=re.search('easy$',s)
# if res!=None:
#     print('Target string ends with Learn')
# else:
#     print('Target string not ends with Learn')

#===================================================

# $ symbol with search()
import re
s = 'Learning python is very EASY'
res=re.search('^Easy',s,re.IGNORECASE)
if res!=None:
    print('Target string ends with Learn')
else:
    print('Target string not easy with Learn')