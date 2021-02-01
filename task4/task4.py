import sys
import re
   
pattern = '.*'.join(map(lambda x: re.escape(x), sys.argv[2].split('*')))
print('OK' if re.fullmatch(pattern, sys.argv[1])  else 'KO')