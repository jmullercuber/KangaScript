Super-Calculator
================

For my 2014-2015 Senior Project, I bring forth a calculator, and it's gonna be awesome


Execution
---------
To run a KangaScript file from the command line, a couple of things.

Currently, you'll need a working version of Python (tested w/ 2.7)
With ksexec.py on your path/ in your directory type, as well as the ks file, type

`$> python ksexec.py test.ks`

print statements are interpreted as python prints, and will be show where ever python would have


Syntax Highlighting
-------------------

I have a file that specifies KangaScript syntax highlighting, for use with gedit.
Plop it in the usr/share/gtksourceview-2.0/language-specs/ folder, restart gedit, and it should be good!
C:/Program Files (x86)/gedit/share/gtksourceview-2.0/language-specs/ folder for gedit for Windows
Thanks to Andrew Schulman for his Stack Overflow answer that got me started: http://superuser.com/a/354684
