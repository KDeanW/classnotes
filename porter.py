import sys
pow=str(open('store.txt').read())
if sys.argv[1]=='1':
    print(pow.count('LISTENING'),'open ports')
if sys.argv[1]=='2' and input()=='yes':
    for i in range(pow.count('LISTENING')):
        print(pow[pow.index('LISTENING')+9:pow.index('/')])
        pow=pow.replace(pow[0:pow.index('\n')+1],'')
