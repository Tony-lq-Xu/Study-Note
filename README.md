# Study-Note
## Markdown language
~test delete~
**bold**
*italic*

[link to Amay](http://cnportal.intranet.local/SitePages/HomePage.aspx)

list
- fist 1
- second 2
  - 2.1
  - 2.2
    - how about this
    - guess
      - deep more
      - what will happen?
 
 quote something:
 > No business too small, no problem too big
 > --IBM
 
 ```python
def myfun(num):
  if num > 0:
    return 'postive'
   else:
    return 'negtive'
```

:camel:
:boom:
:us::cn:

## OMS system
### fixing data
if order line missed in confirm, just add the missing line to confirm interface.

## Vim
### Command
0: cursor to begin of the line
$: cursor to end of the lin

#### Cut and paste:

1. Position the cursor where you want to begin cutting.
2. Press v to select characters, or uppercase V to select whole lines, or Ctrl-v to select rectangular blocks (use Ctrl-q if Ctrl-v is mapped to paste).
3. Move the cursor to the end of what you want to cut.
4. Press d to cut (or y to copy).
5. Move to where you would like to paste.
6. Press P to paste before the cursor, or p to paste after.

Copy and paste is performed with the same steps except for step 4 where you would press y instead of d:

d stands for delete in Vim, which in other editors is usually called cut
y stands for yank in Vim, which in other editors is usually called copy

### search then replace
:%s/Search-Word/Replace-Word/gc

### Example
27iha^esc : input 'ha' 27 times

## Python
### Tips
#### How to get current work directory?
```python
import os
os.getcwd()
```

byte strings hold bytes-based data, not decoded Unicode code point ordinals.

in tkinter, containers are passed in as the first argument when making a new widget; they default to the main window.

## Unix
command can generally be made to run independently and in parallel with the caller by adding an & <br/>
list directory only : ls -d */ <br/>    
execute python script directly with start line as: 
```python
#!/usr/bin/python or
```
or better use enviroment setting
```pyton
#!/user/bin/env python
```

## knowledge
The Document Object Model (DOM) is a cross-platform and language-independent application programming interfacethat treats an HTML, XHTML, or XML document as a tree structure wherein each node is an object representing a part of the document. 
