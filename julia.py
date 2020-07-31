from PIL import Image, ImageDraw
import numpy as np
import math

#Image Size
width = 512
height = 512


image = Image.new('RGB', (width,height), (255,255,255))
draw = ImageDraw.Draw(image)
#pixels = image.load()

#Drawing Area
lx = -2.0
ux = 2.0
ly = -2.0
uy = 2.0

maxiter = 100

frame = 1

for angle in np.arange(0.0, 2*math.pi, 0.25*math.pi):

	for x in range(width):
		for y in range(height):
		
			#Mapping x1 from range [a,b] to x2 in range [c,d]: x2 = (x1-a)*((d-c)/(b-a)) + c 
			a = (x-0)*((ux-lx)/(width-0)) + lx
			b = (y-0)*((uy-ly)/(height-0)) + ly

			z = complex(a,b) #z = a+ib
			c = complex(-1.0 + 0.3*math.sin(angle),0.3*math.cos(angle))
			iter = 0

			while abs(z)<=2 and iter<maxiter:
				z = z*z + c
				iter+=1

			color = 255 - int(iter * 255 / maxiter)
			draw.point([x, y], (color,color,color))
			#pixels[x,y] = (color,color,color)

	image.save("julia_%d.png"%frame, "PNG")
	frame = frame+1


#To convert into GIF
#convert -delay 10 *.png julia.gif