#from PIL import Image
#import pytesseract as pt
import imageio.v3 as iio
import numpy as np

path = '/users/juhi/Downloads/mlassignmentimage.jpg'
f= open("/users/juhi/Documents/ml_assignment_file.txt","w+")
#text = pt.image_to_string(Image.open(image), lang="eng")
image=iio.imread(path)
#image = np.array(image1)
text=[]
s = image.shape
print(s)
h = s[0]
w = s[1]
nc= s[2]
for y in range(h):
	for x in range(w):
		for c in range(nc):
			text.append(image[y][x][c])
f.write(str(w)+'\n')
f.write(str(h)+'\n')
f.write(str(nc)+'\n')
t2 = ", ".join([str(x) for x in text])
f.write(str(t2))
