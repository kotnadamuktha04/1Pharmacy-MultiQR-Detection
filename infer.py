import os
import json
import argparse
from src.utils.qr_detector import detect_qr_codes

def main(input_dir, output_file):
    print("[INFO] Starting inference...")
    print(f"[INFO] Looking in folder: {input_dir}")

    results_all = []
    if not os.path.exists(input_dir):
        print(f"[ERROR] Input directory does not exist: {input_dir}")
        return

    files = os.listdir(input_dir)
    print(f"[INFO] Found {len(files)} files in {input_dir}")

    for filename in files:
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"[INFO] Processing file: {filename}")
            path = os.path.join(input_dir, filename)
            qr_results = detect_qr_codes(path)
            results_all.append({
                "image_id": filename,
                "qrs": qr_results
            })

    if not results_all:
        print("[WARN] No images were processed.")
    else:
        print(f"[INFO] Processed {len(results_all)} images.")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(results_all, f, indent=2)

    print(f"[INFO] QR detection complete. Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Folder with images")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    args = parser.parse_args()

    main(args.input, args.output)
