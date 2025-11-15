import sys
import inspect

def mod1_test1():
    print('mod1_test1')
    print("path : ", inspect.getfile(inspect.currentframe()))
def mod1_test2():
    print('mod1_test2')
    print("path : ", inspect.getfile(inspect.currentframe()))

