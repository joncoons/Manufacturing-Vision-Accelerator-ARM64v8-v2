import os
import glob
import time
import cv2
import easyocr

os.environ["EASYOCR_MODULE_PATH"] ="/ocr_modules"

reader = easyocr.Reader(['en'])

image_directory = "/test_images/en_sample/*"
image_files = glob.glob(image_directory)
begin_job = time.time()
for image_file in image_files:
    start_time = time.time()
    image = cv2.imread(image_file)
    text = reader.readtext(image)
    print(text)
    print("OCR Time: ", time.time() - start_time)

print("Completed 1000 images in: ", time.time() - begin_job)