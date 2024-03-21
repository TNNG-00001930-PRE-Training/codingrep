my_list=[]
for i in range(2000,3200+1):
    if i%7==0 and i%5!=0:
        my_list.append(i)
str1=""
for i in my_list:
    str1=str1+str(i)+" "
print(str1)    

