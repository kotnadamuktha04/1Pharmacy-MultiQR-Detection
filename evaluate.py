import cv2
from pyzbar import pyzbar

def detect_qr_codes(image_path):
    print(f"[INFO] Scanning: {image_path}")
    image = cv2.imread(image_path)
    if image is None:
        print(f"[ERROR] Could not read image: {image_path}")
        return []

    qr_codes = pyzbar.decode(image)
    print(f"[INFO] Found {len(qr_codes)} QR codes.")
    results = []
    for qr in qr_codes:
        x, y, w, h = qr.rect
        value = qr.data.decode("utf-8")
        print(f"[INFO] QR value: {value}, bbox: {[x, y, x + w, y + h]}")
        results.append({
            "bbox": [x, y, x + w, y + h],
            "value": value
        })
    return results
