# Reversed string

# 1.approch by using slicing

# s = "Team brain work is most popular classes"
# print(s[::-1])

# 2. approche by using reversed() function

# s = "Team brain work is most popular classes"
# 
# r = reversed(s)
# 
# #for i in r:
# #    print(i)
# output = ''.join(r)
# print(output)

#==========================================================

# #3. by using while loop
# str = input("Enter the valid string :")
# #s = "Amol"
# output = ''
# i = len(str)-1
# while i >= 0:
#     output = output + str[i]
#     i = i - 1
# print(output)

#==========================================================

# 4. WAP on reveres odrer of words

# s = input("Enter a string : ")
# l = s.split()    # to saperate a individual words
# l2 = l[::-1]     # to reversed a input words
# output = ''.join(l2) # for a output in a single line (by default we are getting output in list form)
# print(output)

#=========================================================

# 5. WAP to reverse internal content of each word

# s = " Durga software solution "
# l = s.split() # for spliting each words
# l2 = []       # for storing after append operation
# for word in l: # for iteration
#     l2.append(word[::-1]) # After reverse operation store value in l2
# output = ' '.join(l2)    # for output in single line instate list form[------]
# print(output)

#=================================================================================

# 6. WAP to reverse every second word of a string

# s = "one two three four five six"
# l = s.split() # split a word for individual operation
# i = 0        # take variable for iteration
# l1 = []      # empty list for output collection
# while i<len(l):   # condition for iteration
#     if i%2 == 0:  
#         l1.append(l[i]) # once condition is satisfy value will store at l1
#     else:
#         l1.append(l[i][::-1]) # if condition is not satisfied even value reversed the position & store into l1
#     i += 1    
# #print(l1)
# output = ' '.join(l1)
# print(output)

#==================================================================================

# # 7. WAP to print the charecters present at even index and odd index saperately for the given string
# 
# s = "Durga software"
# i = 0
# print("The charecter present at odd index :")
# while i<len(s):
#     print(s[i]) # it can be filter even & odd charecter from string
#     i +=2
# 
# i = 1
# print("The charecter present at even index :")
# while i<len(s):
#     print(s[i]) # it can be filter even & odd charecter from string
#     i +=2

# Alternate option by using for loop

# s = "durgasoft"
# 
# for i in range(len(s)):
#     
#     if i%2 == 0:
#         
#         print("The even number of charecters is ",s[i])
#     else: 
#         print("The odd number of charecters on given string is",s[i])

#=======================================================================
 
 # WAP to sort charecters of the sting, first alphabets, symbol & followed by digit
 
#s = "A1D2FT3GHB489"
# s = input("Enter only alphanumeric string ti sort :")
# Alphabets = [] # Take empty list storing sorted elements
# Digits = [] # Take empty list storing sorted elements
#  
# for ch in s: 
#     if ch.isalpha(): # for sorting alphabets
#         Alphabets.append(ch) # for storing it on Alphabets
#     else:
#         Digits.append(ch) # for storing it on Digits
# output = ''.join(sorted(Alphabets)+sorted(Digits)) # for joining concatenate sorted elements
# print(output)

#=======================================================================

#WAP for following requirement
# '''input = a4b3c2    output = aaaabbbcc'''
# 
# #s = "A4B3C2"
# s = input("Enter the required sequence :")
# output = '' # for this type of programs we need to assign empty string for storing the output
# for ch in s:
#     if ch.isalpha(): # for sorting alphabets from given string
#         x = ch
#     else:
#         d = int(ch) # str*str this operation not performed hence we need to convert this into 'int'
#         output = output + x*d
# print(output)

# alternate way :- if we want output in sorted way abc.....z 

# s = input("Enter a string as per expectation :")
# target = ''
# for ch in s:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch)
#         target = target + x*d
# output = ''.join(sorted(target))
# print(output)

#=========================================================================
# WAP for sorted output on given string

# s = input("Enter a string as per expectation :")
# target = ''
# for ch in s:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch)
#         target = target + x*d
# output = ''.join(sorted(target))
# print(output)

#=============================================================================
# WAP to sorted output on below pattern
# input = 'aaaabbbccz'  output = 4a3b2c1z

# s = 'aaaabbbccz'
# previews = s[0] # to store indexing valu of s
# output = ''     # for storing output value
# c = 1   # initial count value
# i = 1   # initial iterate value
# while i <len(s): # condition for comparing lenght of string
#     if s[i] == previews: # for compare condition initial string value == previews store value
#         c = c+1      # if condition is satisfied increament the count value by 1
#     else:
#         output = output + str(c)+previews # for storing output value + string of count value + indexing value
#         previews = s[i] # for index of string
#         c=1    # condition after iniatizing value
#     if i == len(s)-1:  # condition for storing last value in output
#         output = output + str(c)+previews 
#     i = i + 1 # for count increamented by one 
# print(output)

#============================================================================

#WAP for following requirements
# input = a4k3b2 output = aeknbd
# s = input("Enter the required string : ")
# #s = 'a4k3b2'
# output = ''    # for stornig output
# for ch in s:    # condition for iteration
#     if ch.isalpha(): # if charecter is present in output then store into output
#         output = output+ ch 
#         x = ch     # to store ch in x for further comparision
#     else:
#         d = int(ch)   # typecast ch into int 
#         newc = chr(ord(x)+d) # to convert unicode of charecter & add with int value & store it in newc
#         output = output+newc # final value store in output
# print(output)

#==============================================================================

# WAP to remove duplicate charecters from string

# 1st way

# s = 'AAASDDEFFDDRRG'
# output = ''
# for ch in s:
#     if ch not in output:
#         output = output + ch
# print(output)
# 
# # 2nd way
# 
# s = input("Enter a string :")
# l = []
# for ch in s:
#     if ch not in l:
#         l.append(ch) # append is method of list only
#     #output = ''.join(l)
# print(l)

# 3rd way using set ---for this approche we need to individual charecters in string

# s = 'aaddccffeeggbbgfsff'
# s1 = set (s)
# output = ''.join(s1)
# print(output) # duplicates are remove but order of string is no garentee 

#=============================================================================

# WAP to find the numbers of occurance in given string

# 1st way

# s = 'aabbbbbggtttttddd'
# l = []
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# for ch in sorted(l):
#     print('{} occurance {} times'.format(ch,s.count(ch)))

# 2nd way

# s = 'dddffrrddbbaa'
# s1 = set(s)
# print(s1)
# for ch in sorted(s1): # sorted is for arranging the sequence of string
#     print('{} occurs {} times'.format(ch,s.count(ch)))
#     
#=============================================================================

# d = {}
# d['A'] = 100
# d['B'] = 200
# d['A'] = 300
# print(d.get('A'))
# print(d.get('Z'))
# print(d.get('Z',0))
# print(d)

# d = {'A':100,'Z':200,'C':400,'B':500}
# 
# for k,v in d.items():
#     print(k,v)

# WAP for occurance without using count()

#     s = 'AABBBZZZZZDDDDDVVVVVFFFFFFF'
#     d = {}
#     for ch in s:
#         d[ch] = d.get(ch,0)+1
#     for k,v in (sorted(d.items())):
#         print('{} occurs {} times'.format(k,v))
#         
#============================================================================
    
# WAP using dict following below requirement
# input = 'ABAABBCA' output = 4A3B1C

# s = input("Enter a required string :")
# #s = 'ABAABBCA'
# d = {}
# for ch in s:
#     d[ch] = d.get(ch,0)+1 
# #print(d)
# output = ''
# for k,v in d.items():
#     output = output + str(v) + k # for we want required output in digit followed by charecter
# print(output)

#=============================================================================

# WAP find number of occurances of each value present in the given string

# s = input("Enter a input string :") # for dynamic input 
# #s = 'DURGASOFTWARE'
# v = {'a','e','i','o','u','A','E','I','O','U'}
# d = {}
# for ch in s:
#     if ch in v:
#         d[ch] = d.get(ch,0)+1
# #print(d)
# for k,v in sorted(d.items()):
#     print('{} occurs {} times '.format(k,v))

#==============================================================================

# WAP two strings are said to be anagram if both are having same content irrespective of charecters position

# s1 = input("Enter first string : ")
# s2 = input("Enter second string : ")
# if (sorted(s1))==(sorted(s2)):
#     print("both string are anagrams of each others")
# else:
#     print("both strings are not anagram of each others")

#==============================================================================
    
# WAP to check given string is palindrome

# s = input("Enter any string :")
# if s == s[::-1]:
#     print("A given string is palindrome")
# else:
#     print("A given string is not palindrome")

#==============================================================================
    
# WAP to generate a word by using input strings by taking charecters alternately

# s1 = 'abcdefghij'
# s2 = 'xyz'
# s3 = '12345'
# i=j=k=0
# while i<len(s1) or j<len(s2) or k<len(s3):
#     output = ''
#     if i<len(s1):
#         output = output+s1[i]
#         i = i+1
#     if j<len(s2):
#         output = output+s2[j]
#         j = j+1
#     if k<len(s3):
#         output = output+s3[k]
#         k = k+1
#     print(output, end=' ')

#===============================================================================
    



