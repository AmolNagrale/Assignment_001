# Python | Ways to check if element exists in list

# # first approch using for loop
# 
# mylist = [1,2,3,4,5,6]
# 
# compare = 10
# 
# flag = 0
# 
# for i in mylist:
#     if(i == compare):
#         print("Element is exist in given list")
#         flag = 1
#         break
# if flag == 0: 
#         print("Element dose not exist in list")
        
        
#==================================================================
# second approch using in operator

mylist = [1,2,3,4,5,6]

ele = 100

if ele in mylist:
    print("Element exist on list")
else:
    print("Element is not exist on list")




    

