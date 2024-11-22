pow=str(open('store.txt','r').read())
import sys 
if sys.argv[1]=='1':
    print(pow[pow.index('netmask')+8:pow.index('b')])
elif sys.argv[1]=='2':
    print(pow[pow.index(':"')+2:len(pow)-2])
elif sys.argv[1]=='3':
    print(pow[pow.index('broadcast')+10:len(pow)-2])
elif sys.argv[1]=='4':
    print(pow[pow.index('via')+4:pow.index('dev')-1])
elif sys.argv[1]=='5':
    pow=pow[0:pow.index('\n')].replace(' ','')
    print(pow[pow.index('ether')+5:pow.index('ether')+19])
