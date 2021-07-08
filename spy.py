clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
spy = {}
for kind in clothes:   
    if kind[1] in spy.keys():
       spy[kind[1]] =  spy[kind[1]]+1
    else: 
        spy[kind[1]] = 1
count = 1
for i in spy.values():
    count = count * (i+1) 
count = count -1
print(count)