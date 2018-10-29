#Box-Muller method
#to generate gaussian values from the numbers distributed uniformly.

import numpy as np
import matplotlib.pyplot as plt

#generate from uniform dist
np.random.seed()
N = 1000
z1 = np.random.uniform(0, 1.0 ,N)
z2 = np.random.uniform(0, 1.0 ,N)
z1 = 2*z1 - 1
z2 = 2*z2 - 1

#discard if z1**2 + z2**2 <= 1
c = z1**2 + z2**2
index = np.where(c<=1)
z1 = z1[index]
z2 = z2[index]
r = c[index]

#transformation
y1 = z1*((-2*np.log(r**2))/r**2)**(0.5)
y2 = z2*((-2*np.log(r**2))/r**2)**(0.5)

#discard outlier
y1 = y1[y1 <= 5]
y1 = y1[y1 >= -5]
y2 = y2[y2 <= 5]
y2 = y2[y2 >= -5]

#plot
fig = plt.figure()
ax = fig.add_subplot(2,1,1)
ax.hist(y1,bins=30,color='red')
plt.title("Histgram")
plt.xlabel("y1")
plt.ylabel("frequency")
ax2 = fig.add_subplot(2,1,2)
ax2.hist(y2,bins=30,color='blue')
plt.xlabel("y2")
plt.ylabel("frequency")
plt.show()
