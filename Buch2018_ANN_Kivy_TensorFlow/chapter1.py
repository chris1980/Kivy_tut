#Author: 			Christian Sannemann
#Erstellt am: 		17.06.2020
#Zuletzt geändert: 	17.06.2020


#Kapitel 1.1

import matplotlib.pyplot as plt
import numpy as np



rand_img = np.random.uniform(low = 0, high = 3, size = (5,5))
rand_img = np.uint8(rand_img)
hist = np.histogram(rand_img, bins = 4)
plt.bar([0,1,2,3], height= hist[0], align="center", width=0.3)
plt.xticks([0,1,2,3], fontsize = 20)
plt.yticks(np.arange(0, 15,2), fontsize = 20)

plt.show()