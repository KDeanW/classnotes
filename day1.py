input=str(open('inputday1.txt').read()).replace('\n',' ').replace('   ',' ').split(' ')
list1=[]
list2=[]
direction=1
for i in range(len(input)):
    if direction==1:
        list1.append(int(input[i]))
    elif direction==-1:
        list2.append(int(input[i]))
    direction=direction*-1
pairs=[]
distance=[]
total=0
for e in range(len(list1)):
    lowest1=9999999
    lowest2=9999999
    for i in range(len(list1)):
        if list1[i]<lowest1:
            lowest1=list1[i]
        if list2[i]<lowest2:
            lowest2=list2[i]
    list1.pop(list1.index(lowest1))
    list2.pop(list2.index(lowest2))
    pairs.append(lowest1) 
    pairs.append(lowest2)
for i in range(0,len(pairs),2):
    distance.append(abs(pairs[i]-pairs[i+1]))
    total=total+distance[int(i/2)]
print(total)