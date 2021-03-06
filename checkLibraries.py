#"""
#-------------------------------------------------------------------------------
#
#    Authors:    Parshan Pakiman  | https://parshanpakiman.github.io/homepage/
#                Selva Nadarajah  | https://selvan.people.uic.edu/
#                         
#    Licensing Information: The MIT License
#-------------------------------------------------------------------------------
#"""
import imp

listLibs = ['gurobipy',
            'numpy',
            'itertools',
            'time',
            'pandas',
            'os',
            'gc',
            'multiprocessing',
            'functools',
            'scipy',
            'math',
            'sampyl',
            'sys',
            'textwrap',
            'shutil',
            'importlib']
notFound = []
found    = []

for lib in listLibs:
    try:
        imp.find_module(lib)
        found.append(lib)
    except ImportError:
        notFound.append(lib)
   
print("{:<15}\t{:>5}".format('Library','Found'))
print('{:{fill}^{w}}'.format('-',fill='-',w=21))     
for lib in found:
    print("{:<15}\t{:>5}".format(lib,'YES'))
for lib in notFound:
    print("{:<15}\t{:>5}".format(lib,'NO'))
