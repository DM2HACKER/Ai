d1={}
d2={}

n=int(input("Enter how much you insert:"))
for i in range(n):
    key=input("ENter key1:")
    va=input("Enter Value1:")
    d1[key]=va

n=int(input("Enter how much you insert:"))
for i in range(n):
    key=input("ENter key2:")
    va=input("Enter Value2:")
    d2[key]=va
print("Common Key")
if key in d1:
    if key in d2:
        print(key)
