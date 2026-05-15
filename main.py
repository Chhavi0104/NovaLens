from core.capture import capture_image
from core.ocr_engine import extract_text
from core.tts_engine import speak_text

def main():
    image = capture_image()
    text = extract_text(image)
    speak_text(text)

if __name__ == '__main__':
    main()
    