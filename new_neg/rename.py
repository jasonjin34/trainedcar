import os

def main():
    filelist = os.listdir(".")
    # png image list
    png_image_list = []
    jpg_image_list = []
    for it in filelist:
        if it.endswith('.jpeg'):
            jpg_image_list.append(it)
        if it.endswith('.png'):
            png_image_list.append(it)
    currentindex = 500
    jpgindex = 1
    for it in png_image_list:
        filename = 'neg-' + str(currentindex) + '.png'
        os.rename(it, filename)
        currentindex += 1
    for it_jpg in jpg_image_list:
        filename = 'neg-' + str(jpgindex) + '.jpeg'
        os.rename(it_jpg, filename)
        jpgindex += 1
    
        
if __name__ == '__main__':
    main()

