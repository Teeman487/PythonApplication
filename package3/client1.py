# Imporring modules from 2 different packages
import sys
sys.path.append("C:/Users/MR AKINADE AA/PycharmProjects/PythonProject/pythonProject/package1")
from mod1 import *

sys.path.append("C:/Users/MR AKINADE AA/PycharmProjects/PythonProject/pythonProject/package1/package2")
from mod2 import *

display()
show()