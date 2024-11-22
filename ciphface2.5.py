from ciph import handle
import sys
ear=str(open('ear.txt').read())
if sys.argv[1]=="cover":
      ear=handle('1',ear,'1')
      ear=handle('4',ear,'1')
      ear=''.join(filter(str.isdigit, ear))
if sys.argv[1]=='uncover':
      ear=''.join(filter(str.isdigit, ear))
      ear=handle('4',ear,'2')
      ear=handle('1',ear,'2')
print(ear)
