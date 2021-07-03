# Python Ways to remove i’th character from string

# 1.Removing a Character from String using the Naive method

# input_str = "Teambrainworks"
#    
# # Printing original string  
# print ("Original string: " + input_str) 
#    
# result_str = "" 
#    
# for i in range(0, len(input_str)): 
#     if i != 3: 
#         result_str = result_str + input_str[i] 
#    
# # Printing string after removal   
# print ("String after removal of i'th character : " + result_str)

#=========================================================================
# 2. Removal of Character from a String using replace() Method

# str = "Engineering"
#    
#  
# print ("Original string: " + str) 
#    
#  
# res_str = str.replace('e', '') 
#    
#  
# # removes all occurrences of 'e' 
# print ("The string after removal of character: " + res_str) 
#    
# # Removing 1st occurrence of e 
#  
# res_str = str.replace('e', '', 1) 
#     
# print ("The string after removal of character: " + res_str)
# # 
# 
# #==========================================================================
# 
#3. Removal of Character from a String using Slicing and Concatenation

# str = "Engineering"
#    
#  
# print ("Original string: " + str) 
#    
# # Removing char at pos 3 
# # using slice + concatenation 
# res_str = str[:2] +  str[3:] 
#    
#  
# print ("String after removal of character: " + res_str)

# #=========================================================================
# 
# '''4. Removal of Character from a String using join() method and list comprehension
# In this technique, every element of the string is converted to an equivalent
# element of a list, after which each of them is joined to form a string excluding
# the particular character to be removed.'''
# 
# str = "Engineering"
#    
#  
# print ("Original string: " + str) 
#    
# # Removing char at index 2 
# # using join() + list comprehension 
# res_str = ''.join([str[i] for i in range(len(str)) if i != 2]) 
#    
#  
# print ("String after removal of character: " + res_str) 

# #=========================================================================
# 
#5. Removal of character from a string using translate() method

str = 'Engineer123Discipline'
 
print(str.translate({ord(i): None for i in '123'}))

