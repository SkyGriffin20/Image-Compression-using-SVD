# Image Compression using Singular Value Decomposition
# This is a python code that compresses a given image. This reduces the storage size and quality of the image.
# In the end are two graphs showing quality vs size(r)

from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np
import os
plt.rcParams['figure.figsize'] = [16, 8]

# Import image
A = imread(os.path.join("castle.jpg"))

# Convert RGB to grayscale
X = np.mean(A,-1);

img = plt.imshow(X)
img.set_cmap('gray')
plt.axis('off')

# Display grayscale image
plt.show()

# split the matrix into U, S, VT
U, S, VT = np.linalg.svd(X,full_matrices=False)
S = np.diag(S)

j = 0
# Try compression with different k:
for r in (50,75,100,125,150,175,200,300,400,500):
    #Approximation of A
    Xapprox = U[:,:r] @ S[0:r,:r] @ VT[:r,:]
    plt.figure(j+1)
    j += 1
    img = plt.imshow(Xapprox)
    img.set_cmap('gray')
    plt.axis('off')
    plt.title('r = ' + str(r))
    plt.show() 



#Plot singular values graph
plt.figure(1)
plt.semilogy(np.diag(S))
plt.title('Singular Values')
plt.show()

#plot cumulative sum graph
plt.figure(2)
plt.plot(np.cumsum(np.diag(S))/np.sum(np.diag(S)))
plt.title('Singular Values: Cumulative Sum')
plt.show()