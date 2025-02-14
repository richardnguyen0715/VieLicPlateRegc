import cv2
import numpy as np
import os
from pathlib import Path
import glob

#Get the dir path
currDir_path = Path(__file__).parent
testDir_path = currDir_path/'datasets/test'

#Check the path
print("Test path: ", testDir_path)

#Get the Licesen Plate of the first 50 vehicles.
image_paths = sorted(glob.glob(os.path.join(testDir_path/'images', "*.jpg")))[:50]

#Get the Plate position of the first 50 vehicles.
label_paths = sorted(glob.glob(os.path.join(testDir_path/'labels', "*.txt")))[:50]

#Crop the plate 
def yoloToBbox(x_center, y_center, width, height, img_w, img_h):
    x1 = int((x_center - width / 2) * img_w)
    y1 = int((y_center - height / 2) * img_h)
    x2 = int((x_center + width / 2) * img_w)
    y2 = int((y_center + height / 2) * img_h)
    return x1, y1, x2, y2

def cropPlate(image, coordinates):
    img_h, img_w, _ = image.shape
    cropped_plates = []
    for coord in coordinates:
        x1, y1, x2, y2 = yoloToBbox(coord[0], coord[1], coord[2], coord[3], img_w, img_h)
        cropped_plates.append(image[y1:y2, x1:x2])
    return cropped_plates

#Read & Crop & Save The Plates
for i, (img_path, lbl_path) in enumerate(zip(image_paths, label_paths)):
    image = cv2.imread(img_path)
    labels = np.loadtxt(lbl_path, usecols=(1,2,3,4), ndmin=2)

    plates = cropPlate(image, labels)

    for j, plate in enumerate(plates):
        if plate is not None and plate.size > 0:
            cv2.imwrite(os.path.join(currDir_path/'plateset', f'plate_{i}_{j}.jpg'), plate)