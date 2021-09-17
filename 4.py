import numpy as np
a1 = ['aaa', 'bbb', 'ccc']
a2 = ['ppp', 'qqq', 'rrr']
print(np.char.multiply(a1, 2))
print (np.char.multiply(a1, [2, 4, 3]))
print (np.char.multiply(a2, 3))