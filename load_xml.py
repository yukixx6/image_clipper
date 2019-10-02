import cv2 
import numpy as np

path = './info.dat'
neg_path = './bg.txt'
count = 0
one = []
twe = []
mozi = ''
box = []

with open (path, 'r') as f:
	l_strip = [s.strip() for s in f.readlines()]
	for i in range(len(l_strip)):
		for j in range(len(l_strip[i])):
			if l_strip[i][j] == ' ' :
				count += 1
				if count >= 2:
					one.append(mozi)
					mozi = ''
					count = 0
					# space_count = 0
				else:
					mozi = mozi+' '
					# space_count += 1
					
				# if space_count >= 4:


			else:
				mozi = mozi + l_strip[i][j]
				count = 0
		mozi = ''
		twe.append(one)
		one = []

for i in range(len(twe)):
	img_path = twe[i][0].strip()
	img =cv2.imread(img_path)
	for j in range(len(twe[i])):
		# for (x,y,w,h) in twe[i][j]:
		# 	print(x)
		if j <=1:
			pass
		else:
			box = twe[i][j].strip().split()
			box = np.array(box)
			box = [int(n) for n in box]
			# print(box)

			img_bolt = img[box[1]:box[1]+box[3], box[0]:box[0]+box[2]]
			# print(img_bolt)
			bn_path = './pos/'+str(i)+'_'+str(j)+'.jpg'
			cv2.imwrite(bn_path, img_bolt)


with open (neg_path, 'r') as f:
	l_strip = [s.strip() for s in f.readlines()]
	for i in range(len(l_strip)):
		neg_img = cv2.imread(l_strip[i])
		neg_bn_path = './neg/'+'neg_'+str(i)+'.jpg'
		cv2.imwrite(neg_bn_path, neg_img)

