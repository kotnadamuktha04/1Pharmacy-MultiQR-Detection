# Pharmacy Multi-QR Detection

A Python project to **detect and decode multiple QR codes** from images. This tool is designed to help pharmacies or similar applications quickly scan and process multiple QR codes in a single image. It uses **OpenCV** and **pyzbar** for image processing and QR code detection.

---

## Features

- Detect **multiple QR codes** in a single image.
- Decode QR code data automatically.
- Output processed images with QR code bounding boxes.
- Save detection results to an output folder.
- Easy-to-use Python scripts with customizable input/output paths.

---
# Folder structure 

## Repository Structure

1Pharmacy-MultiQR-Detection/
    data/
        demo_images/        # Sample images for testing
    outputs/                # Folder where results are saved
    src/
        utils/
            qr_detector.py  # QR detection functions
        infer.py            # Main script to run detection
    venv/                   # Python virtual environment
    README.md               # Project documentation





---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/kotnadamuktha04/1Pharmacy-MultiQR-Detection.git
cd 1Pharmacy-MultiQR-Detection
python3 -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python src/infer.py --input data/demo_images --output outputs


Dependencies
Python 3.8+
OpenCV (opencv-python)
pyzbar (pyzbar)
numpy
Install all dep
