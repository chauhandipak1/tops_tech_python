d={2:"dipak",3:"dhriti",1:"hetu",4:'shital'}

print(d)
print(d.get(3))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(3))
print(d)
print(d.popitem())
print(d)


d1={5:"shital", 6:"chauhan"}
print(d1)
d.update(d1)
print("udpated dict:",d)

d[44]="chauhan again"
print(d)




for i in d:
    print(i, ":",d[i])
    


