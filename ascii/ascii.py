import cv2
import argparse

parser = argparse.ArgumentParser(description='Convert Image Format')
parser.add_argument('-s', type=str, help='path of the source image')
parser.add_argument('-r', type=float, help='Resize factor')
parser.add_argument('-o', type=str, help='output file name')
args = parser.parse_args()

file = open('img.out.txt', 'w')
resize_factor = args.r or 0.2

_img = cv2.imread('../img/lenna.png')
img = cv2.resize(_img, (0, 0), fx=resize_factor, fy=resize_factor)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


for row in img_gray:
    for pixel in row:
        if(pixel < 80):
            file.write('WW')
        elif(pixel < 120):
            file.write('oo')
        elif(pixel < 200):
            file.write('--')
        else:
            file.write('  ')
    file.write('\n')
