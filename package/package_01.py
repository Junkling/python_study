# 패키지
# from sub.module_ex import mod1_test1, mod1_test2
# __init__.py 는 3.3 까지는 꼭 있어야 패키지로 인식하였으나 이젠 없어도 됨 -> 하지만 하위 호환을 위해 유지하는것이 좋다.
from sub.sub1.module_ex_01 import *
from sub.sub2.module_ex_02 import mod_02_func

mod1_test1()
mod1_test2()

mod_02_func()
