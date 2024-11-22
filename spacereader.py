store=str(open('store.txt', 'r').read()).lower().replace('%','').replace('\n',' ').split(' ')
total=0
store.remove('')
for i in range(len(store)):
               total=total+int(store[i])
print(total,'% used')
if total<70:
    print('your good')
elif total<90:
    print('keep an eye on how much stuff you download')
elif total<99:
    print('this disk is near full, please get a new one')
elif total<101:
          print('this disk is full, get a new one')
else:
          print('how?')
