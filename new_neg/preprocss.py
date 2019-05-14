import cv2 as cv
import os

def resizeImage(filenamelist):
	for filename in filenamelist:
		originimage = cv.imread(filename,0)
		size = originimage.shape
		preheight = size[0]
		prewidth = size[1]
		ratio = 1.0
		ratio_width = prewidth / 100.0
		ratio_height = preheight / 40.0
		if ratio_width >= ratio_height:
			ratio = ratio_width
		else:
			ratio = ratio_height
		current_height = int(preheight / ratio)
		current_width = int(prewidth / ratio)
		resize_image = cv.resize(originimage, (current_width, current_height))
		# cv.imwrite('cars_train/' + filename_string, resize_image)

		delta_height = 40 - current_height
		delta_width = 100 - current_width
		print(delta_height, delta_width)	
		top, bottom = delta_height//2, delta_height - delta_height//2
		left, right = delta_width//2, delta_width - delta_width//2
		#extent boarder
		outputimage = cv.copyMakeBorder(resize_image, top, bottom, left, right, cv.BORDER_CONSTANT,255)
		cv.imwrite(filename, outputimage)
			

def main():
	filelist = os.listdir(".")
	png_image_list = []
	jpeg_image_list = []
	for i in filelist:
		if i.endswith('.png'):
			png_image_list.append(i)
		if i.endswith('.jpeg'):
			jpeg_image_list.append(i)

	resizeImage(png_image_list)
	resizeImage(jpeg_image_list)

if __name__ == "__main__":
	main()
