import tracemalloc
tracemalloc.start()
from ciph import handle
from ciph import force
import sys
import os
import subprocess
if sys.argv[1]=='1':
  print(handle(sys.argv[2],sys.argv[3],sys.argv[4]))
elif sys.argv[1]=='2':
  force(sys.argv[2])                                                                                                                    
