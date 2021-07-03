#First approch 

# mylist = [10,20,30,40,50]
# print(mylist)
# count = 0
# for i in mylist:
#     count +=1
# print("count of total length is :", count)

#========================================================================

# Second approch using len function

# mylist = [10,20,30,40,50,60,1,2,3,4,5,6,6] 
# print("count of given list is :",len(mylist))

#======================================================================

# Third approch using sum map lambda function

# mylist = [10,20,30,40,50,60,1,2,3,4,5,6,6] 
# print(sum(map(lambda x: 1, mylist)))

#=======================================================================

#fourth approch ---     sum of one liner

mylist = [10,20,30,40,50,60,1,2,3,4,5,6,6] 
print(sum(1 for int in mylist))

#=======================================================================
 # fifth approch -- using while loop
# mylist = [10,20,30,40,50,60,1,2,3,4,5,6,6] 

# count = 0
# while mylist[count:]:
#     count +=1
# print(count)

#======================================================================
