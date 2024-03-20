s="python is a good programming language"
s=s.split(" ")
for i in s:
    x=len(i)
    if(x%2==0):
        print(i)