from statspy.basics	import rnorm
from statspy.tests import t_test

# rnorm demo
n = 10 

y = rnorm(n)
print(y)

# t.test demo
y = [1,2,3,4]
t_test(y)