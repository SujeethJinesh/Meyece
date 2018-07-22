import cv2


def main():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Meyece")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Meyece", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

    cam.release()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
