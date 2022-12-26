import os
from os import system as run
import platform
bit = platform.architecture()[0]
run('git pull')
if bit=='64bit':
    run('curl -L https://github.com/islamtiaib/new/blob/main/awm64 -o awm64')
    