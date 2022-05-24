# Create a dictionary from 2 lists, where the elements of 1st list are 
# the keys and the elements of the 2nd list are the corresponding values.

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
# res = dict(zip(list1,list2))
# print ("output : " +  str(res))
a={}
i=0
while i<len(list1):
    a[list1[i]]=list2[i]
    i+=1
print(a)
