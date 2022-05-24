# Q14.Write a Python program to multiply all the items in a dictionary.

d = {
    'a': 10,
    'b': 7,
    'c': 2,
}
a= 1
for i in d:
    a = a*d[i]
print(a)