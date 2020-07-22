# Morsepy
A morse encrypter/decrypter module for python  
  
# How to use  
`pip install morsepy`  
  
## To encrypt to morse:  
``` python
from morsepy import Morsepy

# prints out string as morsecode
print(Morsepy.encrypt('hello world')
```
This would return `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`  
  
## To decrypt from morse  
``` python
from morsepy import Morsepy

# prints out morse code as string
print(Morsepy.decrypt('.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
```
This would return `hello world`  
  
# Formatting Rules  
To make using this module easier it's important to format your morse well:  
* Have one white space between each character  
* Have a slash between each word, you can pad this with white space or not **but it's important you choose one and only use that**  *(e.g '- .... .. ... / .-- --- -. .----. -/.-- --- .-. -.-' won't work)*

## Making morse beeps  
Morsepy can output a morse signal as a series of beeps with the `beep()` funnction  
  
```python
from morsepy import Morsepy

Morsepy.beep('hello world!') #outputs a series of beeps for the morse code of 'hello world!'
```
