#!!!python 2.6 only
from distutils.core import setup   
import py2exe   
import sys   
#includes = ['pybrain.structure.networks.*']   
includes = []  
sys.argv.append("py2exe")   
options = {"py2exe":{ "bundle_files": 1,"includes":includes }}  
            
          
setup(#options = options,   
      zipfile=None,    
      console = [{"script":'mktime.py'}])  
      