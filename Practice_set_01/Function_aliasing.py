# fuction aliasing

def wish(name):
    print("good morning",name)
    
greeting = wish

print(id(wish))
print(id(greeting))
#wish("Amol")
#greeting("Amol")
del wish
# wish("Amol")
greeting("Amol")