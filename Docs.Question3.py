# Q3.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

# n=int(input("enter the n:-"))
# a={}
# i=0


n=int(input("Input a number "))
d = {}
for x in range(1,n+1):
    d[x]=x*x
print(d)
    