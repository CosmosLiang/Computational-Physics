import matplotlib.pyplot as plt
import os,imageio
images = []
filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('1dDiffusion.gif', images,duration=1/60)
