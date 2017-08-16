import os
from decimal import *
from time import *
import numpy as np
import re
import time
import random
import cv2


def count_ones(x):
    return bin(x).count('1')

input_folder = os.path.dirname(os.path.realpath(__file__)) + '/input/'

fnames = os.listdir(input_folder)
images = []
for fname in fnames:
	if fname.endswith(".png"):
		images.append(fname)

count = 0

# Prendo un numero e creo una bitmask in cui ogni bit e' un pixel della matrice 8x8
# Scrivo 1 se il colore e' maggiore di 128, 0 altrimenti. Guarda solo la prima componente (dovrebbe essere bianco e nero)
def to_number(array):
	num = 0
	for i in range(len(array)):
		for j in range(len(array[i])):
			if array[i][j] > 128:
				num = num | (1 << (i*8 + j))

	return num

def compressRLE(array):
	if len(array) < 4:
		return array
	result = []
	i = 0
	while i < len(array)-3:
		if array[i] == array[i+1] and array[i+1] == array[i+2]:
			result.append(255)
			j = i+2
			count = 2
			while j < len(array) and array[j] == array[i] and count < 255:
				count +=1
				j+=1
			result.append(array[i])
			result.append(count)
			i = j
			continue
		elif array[i] == 255:
			result.append(array[i])
			result.append(array[i])
		else:
			result.append(array[i])
		i+=1
	for i in range(len(array)-3, len(array)):
		if i < len(array):
			if array[i] == 255:
				result.append(array[i])
				result.append(array[i])
			else:
				result.append(array[i])
			i+=1
	return result


def generate_tilemap(img_text):
	img_text = compressRLE(img_text)
	s = ''.join(',0x%02x'%w for w in img_text)
	s = re.sub(r",(0x[0-9A-Fa-f][0-9A-Fa-f])((,0x[0-9A-Fa-f][0-9A-Fa-f]){15})", r"\n.db \1\2", s)
	s = re.sub(r"\.db ((0x[0-9A-Fa-f][0-9A-Fa-f],){15}0x[0-9A-Fa-f][0-9A-Fa-f]),((0x[0-9A-Fa-f][0-9A-Fa-f][,]*)+)", r".db \1\n.db \3", s)
	#s = re.sub(r"", r".db \1\n.db \3", s)
	return ".globl _frame"+str(im)+"\n.dw _frame"+str(im)+"\n\n_frame"+str(im)+":\n"+s+"\n\n"

#benchmark
#temp1 = cv2.imread(os.path.dirname(os.path.realpath(__file__))+"\\"+images[0])
#lol = temp1[0:8, 0:8]
#for i in range(10000):
#	10 ^ to_number(lol)
#exit()

tileset = [0, 0xFFFFFFFFFFFFFFFF]
tileset_bucket = [np.zeros((8,8), np.uint8)]*256
tileset_bucket[1] = np.ones((8,8), np.uint8) * 255

tileset_weights = [1.0]*256
blank_image = np.zeros((128,128), np.uint8)
lx = 0
ly = 0
gbdk_frameset_file = ""
image_frames_list = []
# Per ogni immagine (frame)
for im in range(len(images)):
	print("loading image", im)
	pos1 = images[im]
	img_text = []
	temp1 = cv2.imread(input_folder + pos1, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	_,temp1 = cv2.threshold(temp1,127,255,cv2.THRESH_BINARY)
	# L'immagine e' 20x18 tile da 8 pixel (160x144px)
	for j in range(0, 18):
		for i in range(0, 20):
			x = i * 8
			y = j * 8
			# Prendo un tile
			crop_img = temp1[y:y+8, x:x+8]
			num = to_number(crop_img)
			minDist = 999999
			index = 0
			# Per ogni tile gia' presente nel tileset, faccio lo XOR per cercare il tile piu' simile
			for k in range(len(tileset)):
				t = tileset[k]
				mask_distance = count_ones(t^num)
				if mask_distance < minDist:
					minDist = mask_distance
					index = k
			# Se il risultato dello XOR e' > 8 e il tileset non e' gia' pieno, allora salvo lo sprite trovato nel tileset
			if minDist > 2 and len(tileset) < 255:
				tileset.append(num)
				index = len(tileset) - 1
				tileset_bucket[index] = crop_img
				# blank_image[ly:ly+8, lx:lx+8] = crop_img
				# lx += 8
				# if lx >= 128:
				# 	lx = 0
				# 	ly += 8
			# Quando un certo tile del tileset viene scelto, aumento il conteggio degli utilizzi di un certo tile
			tileset_weights[index]+=1
			# tileset_bucket[index] = tileset_bucket[index] + crop_img#.astype(np.uint32, copy=False)
			img_text.append(index)
	gbdk_frameset_file += generate_tilemap(img_text)
	image_frames_list.append(img_text)

# print(tileset_bucket[25].max(), tileset_bucket[25].min(), tileset_bucket[25] - tileset_bucket[25].min())
result = []
# metodo pesi
# i = 0
# for tile in tileset_bucket:
# 	tile = tile.astype(np.float32, copy=False)
# 	tile = (tile / (tileset_weights[i]))*255
# 	tile = tile.astype(np.uint8, copy=False)
# 	result.append(tile)
# 	i+=1

# metodo medie (migliore)
for tile in tileset_bucket:
	_min = tile.min()
	_max = tile.max()
	_med = _max - _min
	if _med == 0:
		_med = 1
	tile = (tile - _min)
	tile = tile.astype(np.float32, copy=False)
	tile = (tile / (_med))*255
	tile = tile.astype(np.uint8, copy=False)
	result.append(tile)

result[0] = np.zeros((8,8), np.uint8)
result[1] = np.ones((8,8), np.uint8) * 255

out_file = open("./output/bg.s","w")
out_file.write(gbdk_frameset_file)
out_file.close()

# Creo il tileset e lo salvo
k = 0
for j in range(16):
	for i in range(16):
		x = i*8
		y = j*8
		blank_image[y:y+8, x:x+8] = result[k]
		k+=1

cv2.imwrite('./output/tileset.png', blank_image)

# Ora ricreo tutti i fotogrammi usando il tileset (quello che farebbe GBDK)
for im in range(len(images)):
	image_name = images[im]
	image_frames = image_frames_list[im]
	print("Saving frame", image_name)
	pos1 = images[im]
	img_text = []
	image = cv2.imread(input_folder + image_name, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	# image_frames_list[]
	w = 0
	for j in range(0, 18):
		for i in range(0, 20):
			tile_index = image_frames[w]
			x = i * 8
			y = j * 8
			image[y:y+8, x:x+8] = result[tile_index]
			w += 1
	cv2.imwrite('./output/frames/' + image_name, image)
