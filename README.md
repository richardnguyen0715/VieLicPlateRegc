# VieLicPlateRegc
Vehicle License Plate Recognition

---

### STATEMENT OF WORK
Last updated: 13/02/2025.
#### Member:
Nguyen Anh Tuong.
#### Topic:
Recognizing license plates from images extracted from cameras through the YOLOv11 model and OCR.
#### Work:
* Dataset: [Link](https://universe.roboflow.com/mgm/licence-late-detection)
* Scope of work:
  * Data collection.
  * Data preprocessing.
  * Recognizing license plates.
  * Recognizing the correct numbers and digits.
  * Providing final results.

---
#### Usage
1. Download dataset [here.](https://universe.roboflow.com/mgm/licence-late-detection)
2. Settings the folder name: datasets\
3. Download pytesserat [here.](https://github.com/UB-Mannheim/tesseract) 
4. Create a python environment: `python -m venv env`
5. Start the environment in cmd: `env\Scripts\activate`
6. Install needed libraries: `pip install -r requirements.txt`
7. Try `LicensePlateDetection` file on your own.
8. try `LicensePlateRecognition` file on your own.
