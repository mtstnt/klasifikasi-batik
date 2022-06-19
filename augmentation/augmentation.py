import os
import sys
from PIL import Image

def mkdir_if_not_exist(path):
	if not os.path.exists(path): os.mkdir(path)

base_path = sys.argv[1] if len(sys.argv) > 1 else "./dataset/"
output_path = sys.argv[2] if len(sys.argv) > 2 else "./augmented/"

mkdir_if_not_exist(output_path)

regions = os.scandir(base_path)

for region in regions:
	print("REGION:", region.name)
	class_per_region = []
	if not region.is_dir():
		print("Tidak ada subfolder per provinsi")
		exit(1)

	mkdir_if_not_exist(output_path + region.name)

	for subclass in os.scandir(base_path + region.name):
		class_per_region.append(subclass.name)
		print("SUBCLASS:", subclass.name)

		mkdir_if_not_exist(output_path + region.name + "/" + subclass.name)

		images = []

		if not subclass.is_dir():
			print(f"Subclass {subclass.path} is not a directory.")

		for image_file in os.scandir(base_path + region.name + "/" + subclass.name):
			img = Image.open(base_path + region.name + "/" + subclass.name + "/" + image_file.name)
			
			h_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
			v_flipped = img.transpose(Image.FLIP_TOP_BOTTOM)

			h_flipped.save(output_path + region.name + "/" + subclass.name + "/h_" + image_file.name)
			v_flipped.save(output_path + region.name + "/" + subclass.name + "/v_" + image_file.name)