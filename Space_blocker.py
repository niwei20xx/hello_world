import numpy as np
import random
#
a=np.arange(16)
b=a.copy()
np.random.shuffle(b)
b=b.reshape(4,4)
print(b)
