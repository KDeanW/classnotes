import sys
face=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
bag=['a','a1','b','b1','b2','a2','y','u','n','b3','h','a3','y1','o','b4','d','r','g','i','y2','p','v','r','s','o1','k']
print(sys.argv)
read=list(sys.argv[2])
if sys.argv[1]=='1':
    bond=0
    while bond<len(read)-1:
        merg=str(read[bond])+str(read[bond+1])
        eyes=merg in bag
        if eyes==True:
            read[bond]=merg
            read.pop(bond+1)
        bond=bond+1
    for i in range(len(read)):
        if read[i] in bag:
            read[i]=face[bag.index(read[i])]
elif sys.argv[1]=='2':
    for i in range(len(read)):
        if read[i] in face:
            read[i]=bag[face.index(read[i])]
else:
    print("bad directional input. use '2' to encript and '1' to decript")
print('' .join(read))
