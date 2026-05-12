import cv2

def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not opening. Try again later.")
        return None

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Frame not received. Try again later.")
            break
        
        cv2.imshow('Video Feed', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        elif key == ord(' '):
            print("Image captured successfully.")
            cap.release()
            cv2.destroyAllWindows()
            return frame
        
    cap.release()
    cv2.destroyAllWindows()

    return None

if __name__=='__main__':
    image = capture_image()