# Write a Python script to print a dictionary where the keys are numbers    
# between 1 and 15 (both included) and the values are square of keys.
a=int(input("enter the number:-"))
b = {}
for x in range(1,a+1):
    b[x]=x*x
print(b)