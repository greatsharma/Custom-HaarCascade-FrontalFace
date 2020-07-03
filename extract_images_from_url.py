import os
import cv2
import argparse
import requests
from imutils import paths


ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
	help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")
args = vars(ap.parse_args())

rows = open(args["urls"]).read().strip().split("\n")

total = 0
for url in rows:
	try:
		r = requests.get(url, timeout=60)
		p = os.path.sep.join([args["output"], f"city_{total}.jpg"])
		f = open(p, "wb")
		f.write(r.content)
		f.close()
		print("downloaded: {}".format(p))
		total += 1
	except Exception as e:
		print("\nerror downloading {}...skipping\n".format(p))

for imagePath in paths.list_images(args["output"]):
	delete = False
	try:
		image = cv2.imread(imagePath)
		if image is None:
			delete = True
	except:
		delete = True
	if delete:
		print("deleting {}".format(imagePath))
		os.remove(imagePath)