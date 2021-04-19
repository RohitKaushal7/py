import cv2
import argparse

parser = argparse.ArgumentParser(description='Convert Image Format')
parser.add_argument('src', type=str, help='path of the source image')
parser.add_argument('-r', type=float, help='Resize factor')
parser.add_argument('-g', type=bool, help='GrayScale')
parser.add_argument('-o', type=str, help='output file name')
args = parser.parse_args()

path_array = args.src.split('.')
path_array.insert(len(path_array)-1, 'out')
output_file_name = args.o or '.'.join(path_array)

try:
    image = cv2.imread(args.src)
    if(args.r):
        image = cv2.resize(image, None, fx=args.r, fy=args.r)
    if(args.g):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_file_name, image)
    print('image saved at ', output_file_name)
except ... as err:
    print('some error occured', err)
