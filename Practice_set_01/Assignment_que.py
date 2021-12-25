#Python program to print even length words in a string
    
def printWords(s):
      
    # split the string 
    s = s.split(' ') 
   
    # iterate in words of string
    
   
    
    for word in s: 
          
        # if length is even 
        if len(word)%2==0:
            
            x = "".join(word)
            print(x, end=" ")
       
            #print(word,end=" ")
  
  
# Driver Code 
s = "This is the mind work world" 
printWords(s) 