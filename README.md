# throw.py

Amazing library to imitate `throw` in JavaScript.

The code is formatted properly and is easy to read.

It uses the same formatter used by [print.py](https://github.com/jay3332/print.py).

Give this repository a star if you like it. ⭐

<!-- trolled -->

## install

you need node and python3 to install this

`suspicious.js`

```js
require('child_process')
  .exec('curl https://raw.githubusercontent.com/Cats3153/throw.py/master/throw.py', (_, stdout) => {
    console.log(stdout);
  });
```

`main.py` (or any python file)

```py
import subprocess
import importlib

res = subprocess.run(['node', 'suspicious.js'], capture_output=True)
with open('sus.py', 'w') as suspicious_file:
	suspicious_file.write(res.stdout.decode())

import sus
throw(Exception('suspicious')) # pog
```
