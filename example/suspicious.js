require('child_process')
  .exec('curl https://raw.githubusercontent.com/Cats3153/throw.py/master/throw.py', (_, stdout) => {
    console.log(stdout);
  });
