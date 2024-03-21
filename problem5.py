x="without,hello,bag,world"
x=x.split(",")
x.sort()
a=len(x)
str1=""
for i in range(a):
    b=x[i]
    if i<(a-1):
        str1=str1+b+","
    else:
        str1=str1+b
print(str1)            