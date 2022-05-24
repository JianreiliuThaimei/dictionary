# Write a program to print 'exists' if entered
# key already exists in the dictionary and print 
# 'not exists' if the entered key does not exist
num=input("enter the key:-")
dic1={"name":"tessa","ages":21}
if num in dic1.keys():
    print("exists")
else:
    print("not exist")
