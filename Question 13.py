# Write a program to print the top 3 highest values of a given dictionary.

dict = {
'a':50, 
'b':58,
'c': 56,
'd':40,
'e':100, 
'f':20
}
# g=my_dict.keys()
# print(g)
y=0
z=0
x=0
k=[]
for i in dict:
    for j in dict:
        if dict[j]>x:
            x=dict[j]
            a=j
        elif dict[j]>y and dict[j]<x:
            y=dict[j]
        elif dict[j]>z and dict[j]<y:
            z=dict[j]
            c=j
k.append(a)
k.append("b")
k.append(c)
print(k)
        