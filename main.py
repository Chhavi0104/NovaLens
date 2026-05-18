from core.capture import capture_image
from core.ocr_engine import extract_text
from core.tts_engine import speak_text
from core.scene_description import describe_image

def main():
    choice = 1
    
    while choice != 0:
        print('Press 1 for text reading')
        print('Press 2 for scene description')
        print('Press 0 for exit')

        choice = int(input('/nEnter your choice: '))

        if choice == 1:
            image = capture_image()
            text = extract_text(image)
            speak_text(text)

        elif choice == 2:
            image = capture_image()
            text = describe_image(image)
            speak_text(text)

        elif choice == 0:
            print('Thabk you for trying NovaLens')
            break

        else:
            print('Invalid choice. Please try again.')
   
if __name__ == '__main__':
    main()
    