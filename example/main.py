import subprocess
import importlib

res = subprocess.run(['node', 'suspicious.js'], capture_output=True)
with open('sus.py', 'w') as suspicious_file:
  suspicious_file.write(res.stdout.decode())

import sus
throw(Exception('suspicious')) # pog
