import paddleocr

ocr = paddleocr.PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

def extract_text(image):
    if image is None:
        print("No image received for OCR.")
        return ""

    results = ocr.ocr(image)

    detected_text = []

    for line in results[0]:
        text = line[1][0]
        detected_text.append(text)

    final_text = " ".join(detected_text)

    return final_text