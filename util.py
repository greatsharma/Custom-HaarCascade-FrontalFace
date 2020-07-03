import os
import cv2
import shutil


# count = 0
# for dir_ in os.listdir("google_images/"):
#     for img_name in os.listdir("google_images/"+dir_+"/"):
#         source = "google_images/"+dir_+"/"+img_name
#         try:
#             img = cv2.imread(source, 0)
#             img = cv2.resize(img, (250, 250))
#             cv2.imwrite(f"neg/neg_{count}.png", img)
#             count += 1
#         except Exception as e:
#             print(e)
#             print(source, end="\n\n")

# print(count)


# count = 0
# for img_name in os.listdir("fer_/"):
#     try:
#         img = cv2.imread("fer_/"+img_name, 0)
#         img = cv2.resize(img, (96,96))
#         cv2.imwrite(f"fer/fer_{count}.png", img)
#         count += 1
#     except Exception as e:
#         print(e)
#         print(img_name)

# print(count)


count = 0
img_size = set()
for image_name in os.listdir("pos/"):
    try:
        img = cv2.imread("pos/"+image_name, 0)
        img_size.add(img.shape)
        count += 1
    except Exception:
        print(image_name)

print(img_size, count)


# import os
# from PIL import Image

# count = 0
# for infile in os.listdir("jaffe/"):
#     print("file : ", infile)
#     if infile[-4:] == "tiff":
#        outfile = f"jaffe_/jap_{count}.png"
#        im = Image.open("jaffe/" + infile)
#        print("new filename : ",outfile)
#        out = im.convert("RGB")
#        out.save(outfile, "png", quality=90)
#        count += 1
#     else:
#         print("in else")


# count = 0
# for image_name in os.listdir("jaffe_/"):
#     img = cv2.imread("jaffe_/"+image_name, 0)
#     w, h = img.shape
#     img = img[int(w*0.2): int(w*0.9), int(h*0.25): int(h*0.75)]
#     cv2.imwrite(f"jaffe/jap_{count}.png", img)
#     count += 1

# print(count)


# count = 0
# for dir_ in os.listdir("datasets/"):
#     for img in os.listdir("datasets/"+dir_+"/"):
#         source = "datasets/" + dir_ + "/" + img
#         dest = "pos/"
#         shutil.copy(source, dest)
#         count += 1

# print(count)