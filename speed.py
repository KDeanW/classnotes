argue=str(open('store.txt','r').read())
argue=argue[argue.index('Download:')+10:argue.index(' Mbit/s')]
if float(argue)<35:
    print('Your download speed is slow')

