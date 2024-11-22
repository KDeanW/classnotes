import tracemalloc
tracemalloc.start()
import time
import itertools
face='abcdefghijklmnopqrstuvwxyz'
cy=list(face)
book=(str(open('diction.txt').read()).lower()).replace('\n','|')
global clean
clean=''
dir=0,1,-1
one=1,'1'
two=2,'2'
def cabbage_bag():
  mouth=''
  al=0
  pha=1
  bet=0
  for i in range(len(face)):
    cy[i]=(((al)*-1)+i)
    bet=pha
    pha=al
    al=pha+bet
    #print[face[cy[i]]]
    while cy[i]<0:
      cy[i]=cy[i]+len(face)
    inte= str(mouth.count(face[cy[i]])).replace('0','')
    letter=face[cy[i]]
    cy[i]=str(letter)+inte
    mouth=mouth+cy[i]

def caesar(shift):
  for i in range(len(face)):
    cy[i]=(i+abs(shift))
    while int(cy[i])>0:
      cy[i]=cy[i]-len(face)
    cy[i]=face[cy[i]]

def Vigenère(read,way,vigen):
  cap=list(read)
  read=list(read.lower())
  acfr=0
  vigen=''.join(filter(str.isalpha,vigen))
  for i in range(len(read)):
    if (read[i] in face):
      read[i]=int(face.index(read[i])+(face.index(vigen[i-acfr])*way))
      if read[i]>(len(face)-1):
        read[i]=read[i]-len(face)
      if int(read[i])<0:
        read[i]=read[i]+len(face)
      read[i]=str(face[int(read[i])])
      if cap[i]==cap[i].upper():
        read[i]=read[i].upper()
    else:
      acfr=acfr+1
  return ''.join(read)
def ASCII(rad,way,bacon=False):
  nary=[]
  read=str(rad)
  if way==1:
    bary=''.join(format(ord(i), '08b') for i in read)
    if bacon==True:
      bary=bary.replace('0','a').replace('1','b')
  else:
    for i in range(len(read)):
      if not read[i] in nary:
        nary.append(read[i])
      if len(nary)>2:
        nary=None
        break
    if not nary==None:
      if bacon==True:
        read=read.replace('a','0').replace('b','1')
      bary=''.join(chr(int(read[i*8:i*8+8],2)) for i in range(len(read)//8))
    else:
      bary='nonASCII/nonbacon'
  return bary
def txt(txt):
  if '.txt'in txt:
    txt=str(open(txt).read())
  return txt
def scribe(read,way):
  read=txt(read)
  cap=list(read)
  read=list(read.lower())
  i=0
  while i<len(read)-1:
    if (read[i]+read[i+1] in cy):
      read[i]=str(read[i])+str(read[i+1]) 
      read.pop(i+1)
      cap.pop(i+1)
    i=i+1
  if way in one:        #encryption
    for i in range(len(read)):
      if read[i] in face:
        read[i]=(str(cy[face.index(read[i])]))
  elif way in two:      #decryption
    for i in range(len(read)):
      if read[i] in cy:
        read[i]=(str(face[cy.index(read[i])]))
  for i in range(len(read)):
    if cap[i]==cap[i].upper():
      read[i]=read[i].upper()
  return ''.join(read)
def handle(wat,read,way):
  if wat=='1':
    cabbage_bag()
  elif wat=='2':
    caesar(int(input('what is the shift value\n')))
  elif wat=='3':
    return Vigenère(read,dir[int(way)],txt(input('what is the cipher key\n')).lower())
  elif wat=='4':
    return ASCII(read,dir[int(way)])
  elif wat=='5':
    return ASCII(read,dir[int(way)],True)
  return scribe(read,way)
'''   uncomment to test ciphers | All=It's Working '''
#print(handle('1',"Ny2'i R1b4ghnoy",2))
#print(handle('2',"Lw'v Zrunlqj",2)) #shift value=3
#print(handle('3',"Bx'k Pweqbry",2)) #key=Testingtest
#print(handle('4','010010010111010000100111011100110010000001010111011011110111001001101011011010010110111001100111',2))
#print(handle('5','abaabaababbbabaaaabaabbbabbbaabbaabaaaaaabababbbabbabbbbabbbaabaabbababbabbabaababbabbbaabbaabbb',2))
def verify(written, shift=None):
  global clean
  ac=0
  inac=written.split(' ')
  wrote=list(written.lower())  
  val=0
  while val<len(wrote):
    if (not wrote[val] in face) and (not wrote[val]==' '):
      wrote.pop(val)
    else:
      val=val+1
  sentance=''.join(wrote).split(' ')
  for i in range(len(sentance)):
    if str('|'+sentance[i]+'|') in book:
      inac[i]=' '*len(inac[i])+' '
      ac=ac+1
    else:
      inac[i]='^'*len(inac[i])+' '
  if (ac/len(sentance)*100)>=50:
    digi=(ac/len(sentance))*100
    written=written+' | '+ str(digi)+' accurate'
    if not shift==None:
      print(shift)
    print(written)
    print(''.join(inac)+'|', 'inaccuracies')
    clean=''
  elif clean=='':
    print('inaccurate')
    clean=' '
#verify("It's Working")
def force(unread):
  global clean
  cabbage_bag()
  print('Cabbage Bag:')
  verify(scribe(unread,'2'))
  print('caesar Cipher:')
  clean=''
  for i in range(1,len(face)):
    label='shift: '+str(i)
    caesar(i)
    verify(scribe(unread,'2'),label )
  clean=''
  print('ASCII/Bacons Cipher:')
  verify(ASCII(unread,-1,True))
  clean=''
  if len(unread)<9:
    start=time.time()
    print('Vigenère:')
    combo=list(itertools.combinations_with_replacement(face, len(''.join(filter(str.isalpha,unread)))))
    for i in range(len(combo)):
      if not combo[i][0]==combo[i][len(combo[i])-1]:
        label='key: '+str(''.join(combo[i]))
        verify(Vigenère(unread,-1,''.join(combo[i])),label)
    print(time.time()-start, 'seconds taken for Vigenère cipher' )
#force("ny2'i r1b4ghno bb4ggb2by2a3o1")
#force("lw'v zrunlq fruuhfwob")
#force("010010010111010000100111011100110010000001010111011011110111001001101011011010010110111000100000011000110110111101110010011100100110010101100011011101000110110001111001")
#force("abaabaababbbabaaaabaabbbabbbaabbaabaaaaaabababbbabbabbbbabbbaabaabbababbabbabaababbabbbaaabaaaaaabbaaabbabbabbbbabbbaabaabbbaabaabbaabababbaaabbabbbabaaabbabbaaabbbbaab")
#force("Xidtm")
#force("abba")
