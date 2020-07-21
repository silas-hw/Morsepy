from distutils.core import setup

#get readmefile
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
  
setup(
  name = 'morsepy',         
  packages = ['morsepy'],  
  version = '0.1',      
  license='MIT',       
  description = 'A morse decrypter and encrypter module for python',  
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'silas-hw',                   
  author_email = 'silas.hayes.williams@gmail.com',      
  url = 'https://github.com/silas-hw/Morsepy',   
  download_url = 'https://github.com/silas-hw/Morsepy/archive/v0.2.tar.gz',   
  keywords = ['morse', 'decrypt', 'encrypt'],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)