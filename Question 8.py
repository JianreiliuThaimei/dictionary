# Take input of name and marks of 10 students 
# and store to a dictionary.
# a={
# 'sonu':85,
# 'Kartik':90,
# 'Deepak':96,
# 'Aman':76,
# 'Somesh':60,
# 'Umesh':85,
# 'Amarpal':70,
# 'Roshan':57,
# 'Riyaz':98,
# 'Shabid':56
# }

i=1
a=[]
b=[]
while i<=10:
    user=input("enter the name:- ")
    user1=int(input("enter the mark of the student:-"))
    a.append(user)
    b.append(user1)
    j=0
    c={}
    while j<len(a):
        c[a[j]]=b[j]
        j+=1
    i+=1
print(c)

# i=1
# a=[]
# b=[]
# while i<=3:
#     user=input("enter the user name:")
#     user1=int(input("enter the mark of the student:"))
#     a.append(user)
#     b.append(user1)
#     j=0
#     c={}
#     while j<len(a):
#         c[a[j]]=b[j]
#         j=j+1
#     i=i+1
# print(c)