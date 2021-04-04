from PIL import Image
import random
import matplotlib.pyplot as plt

%matplotlib inline

img = Image.new( 'RGB', (500,500), "black")
pixels = img.load()
colors = []

for i in range(img.size[0]):
    for j in range(img.size[1]):
        #c = random.randrange(255)
        c = random.gauss(127,30)
        c = round(c)
        colors.append(c)
        pixels[i,j] = (c,c,c)
        
bins = range(255)

colors.sort()

print(colors)

plt.hist(colors,bins,histtype="step")
#plt.xticks(range(0,255,50))

img.show()
