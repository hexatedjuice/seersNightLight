#This script was made for the 2020 NASA Rocket Apps Hackathon.
#The SustainableSeers' goal is to analyze and prepare graphics on
#how COVID-19 affected the UN's SDG #11.
#By hexatedjuice | https://github.com/hexatedjuice

from PIL import Image
import sys
import cv2
import numpy as np

files = sys.argv[1:]
values = []

def main():
	clean(files)
	analyze(files)
	report(values)

def clean(stuff):
	tmp = []
	for a in stuff:
		im = cv2.imread(a)

		#smooth images by closing and opening w enlarging kernel
		morph = im.copy()
		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
		morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)
		morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)
		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

		# morph gradient and channel split
		gradient_image = cv2.morphologyEx(morph, cv2.MORPH_GRADIENT, kernel)

		image_channels = np.split(np.asarray(gradient_image), 3, axis=2)
		channel_height, channel_width, _ = image_channels[0].shape
		for i in range(0, 3):
		    _, image_channels[i] = cv2.threshold(~image_channels[i], 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
		    image_channels[i] = np.reshape(image_channels[i], newshape=(channel_height, channel_width, 1))

		image_channels = np.concatenate((image_channels[0], image_channels[1], image_channels[2]), axis=2)

		newimg_name = str(a.split('.')[:1]).translate({ord(x): None for x in "'[]"}) + '_cleaned.png'
		cv2.imwrite(newimg_name, image_channels)
		tmp.append(newimg_name)
	global files
	files = []
	files = tmp


def analyze(files):

	for i in files:
		im = np.array(Image.open(i).convert('1').convert('RGB'))
		white = [255,255,255]
		black = [0,0,0]

		#matching pixels to set rgb values
		result = np.count_nonzero(np.all(im==white,axis=2))
		result2 = np.count_nonzero(np.all(im==black,axis=2))
		values.extend([result,result2])

def report(stuff):
	for i in range(0,len(stuff),2):
		percent = str(float(stuff[i+1]) / float(stuff[i]+ stuff[i+1]) * 100)[:5] + '%'
		print(files[int(i/2)].replace('_cleaned', '') + ' has ' + percent + ' illuminated')

if __name__ == "__main__":
	main()
