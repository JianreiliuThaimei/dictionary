# Take a list having dictionary elements as 
# shown below (Sample Data) and then store all
# the unique values into a list and print.

c=[
 {"first":"1"}, 
 {"second": "2"}, 
 {"third": "1"}, 
 {"four": "5"}, 
 {"five":"5"}, 
 {"six":"9"},
 {"seven":"7"}
]
i=0
print(len(c))
j=0
a=[]
while i<len(c):
    for j in c[i]:
        if c[i][j] not in a:
            a.append(c[i][j])
    i+=1
print(a)
