import tracemalloc
tracemalloc.start()
from ciph import handle 
from ciph import force
while 1==1:
  wow=input('do you know what cipher you need(yes/no)\n')
  if wow.lower()=='yes':
    print(handle(input('what type of cipher \n1.cabbage bag 2.caesar cipher 3.Vigenère cipher 4.binary 5.Bacons cipher\n'),input('what is your input\n'),input('do you need \n1.encyption, 2.decryption \n')))
  elif wow.lower()=='no':
     force(input('(Vigenère cipher decryption will not be attempted if letters in input exceeds 9 for sake of not taking forever)\nwhat do you need solved\n'))
'''cabbage bag test 
        Ny2'i R1b4ghnoy
   caesar chipher test
        shift=3
        Lw'v Zrunlqj
   binary test
        010010010111010000100111011100110010000001010111011011110111001001101011011010010110111001100111
   bacons test
        abaabaababbbabaaaabaabbbabbbaabbaabaaaaaabababbbabbabbbbabbbaabaabbababbabbabaababbabbbaabbaabbb
   Vigenère test 
        key=Testingtest
        Bx'k Pweqbry
all of them = It's Working
'''
