# Pyssword
I guess we can call it Pissword.

# Installation
I would recommened moving both files to `/usr/bin/` if you are going to use it often (why?). Also you can rename them and not
include `.py` because they have `#!/usr/bin/python`, but if it doesn't work after that:
Run `which python`
if that outputs `/bin/python`
then add `#!/bin/python` to the top of the files.
## pyssword-minimal.py
"`pysword-minimal [password length (password_len)] [save password (y/N)]`"
You can pipe the output of that into xclip so you can copy and paste. For example:
"`pyssword-minimal 28 N | xclip -selection clipboard`"
## pyssword.py
Instructions when program is run.