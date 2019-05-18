#isBinary
#ar=[12,14,1,2,54]
#sum=0
#for num in ar:
#    temp=str(num)
#    sum=0
#    for i in range(len(temp)):
#        sum=sum+int(temp[i])
#    if(sum>len(temp)):
#        return(1)
#    else:
#        return(0)
#    sum=0

#Longest substring in string
subs=[]
temp=[]
flag=0
str='1100010111011'
for i in range(len(str)):
    
    if int(str[i])==1:
        subs.append(str[i])
        flag=1
        sublen=len(subs)
        print("before:",temp,"tl",len(temp),"subl:",sublen)
        if sublen>len(temp):
            temp=subs
        print("after:",temp,"tl",len(temp),"subl:",sublen)
    if int(str[i])==0:
        flag=0
    if flag==0:
        sublen=len(subs)
        #print("sublen:", end=" ")
        #print(sublen)
        ##print("Templen (before update):", end=" ")
        #print(len(temp))
        if sublen>=len(temp):
        #    #print("sublen:", end=" ")
        #    #print(sublen)
        #    print("Templen (before update):", end=" ")
        #    print(len(temp))
             temp=subs
        #    print("Templen (after update):", end=" ")
        #    print(len(temp))
        #print("sub:", end =" ")
        #print(subs,len(subs))#prints only uptil penultimate substring
        del subs[0:sublen]
        sublen=len(subs)
        print("sub after del:", sublen)
    #print(subs,"Flag:", flag)
#print("temp:", end =" ")
print(temp,len(temp)) #return last substring
