# Write a program to sort a dictionary in ascending
# or descending according to its values .

# ASCENDING ORDER
a={'bijender':45,'deepak':60,'param':20,
 ';''anjili':30,'roshini':50}
for i in a:
    for j in a:
        if a[j]<a[i]:
            a[j],a[i]=a[i],a[j]
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
for i in a:
    for j in a:
        if a[j]>a[i]:
            a[j],a[i]=a[i],a[j]
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)


