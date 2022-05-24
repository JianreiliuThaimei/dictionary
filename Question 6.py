# Write a program to remove duplicate keys.

dic={"ball":"red",
     "bat":4,
     "wickets":8,
     "ball":"green",
     "bat":3}
print(dic)
a = []
res = dict()
for key, val in dic.items():
    if val not in a:
        a.append(val)
        res[key] = val
print("remove : " + str(res)) 