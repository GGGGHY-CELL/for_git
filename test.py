list = [11,13,10,4,6,7,19,12,15,8]
print(list)
print(list[0],list[9],list[2])
print(len(list))
print("summa:",sum(list), "min:",min(list), "max:",max(list))
for i, item in enumerate(list):
    if i % 2 == 0:
        print(i,item)
safa = sorted(list)
print(safa)
da = list[::-1]
print(da)